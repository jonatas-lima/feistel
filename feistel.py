import random
from keys import KeysGenerator

BLOCK_SIZE = 8
ITERATIONS = 4
SEED = '1010101010101010'

random.seed(SEED)


class Feistel:
    def __init__(self, secret_key: int, iterations: int = ITERATIONS, block_size: int = BLOCK_SIZE) -> None:
        self.__iterations = iterations
        self.__block_size = block_size

        kg = KeysGenerator(secret_key)
        self.__keys = kg.generate_keys()

    def encrypt(self, plain_text: str) -> str:
        first_half_slice, second_half_slice = self.__half_slices(plain_text)
        encrypted_text = plain_text

        for i in range(self.__iterations):
            l0, r0 = encrypted_text[first_half_slice], encrypted_text[second_half_slice]
            e = self.__f(r0, i)
            l1, r1 = r0, self.__xor(l0, e)
            encrypted_text = l1 + r1

        return encrypted_text

    def decrypt(self, encrypted_text: str) -> str:
        first_half_slice, second_half_slice = self.__half_slices(encrypted_text)
        plain_text = encrypted_text

        for i in range(self.__iterations - 1, -1, -1):
            r0, l0 = plain_text[first_half_slice], plain_text[second_half_slice]
            e = self.__f(l0, i)
            l1, r1 = l0, self.__xor(r0, e)
            plain_text = l1 + r1

        return plain_text

    def __f(self, text: str, round: int) -> str:
        key = self.__keys[round]
        result = ''
        stop = False

        for i in range(0, len(text), self.__block_size):
            for j in range(self.__block_size):
                try:
                    k = self.__g(text[i+j], key)
                    result += k
                except IndexError:
                    stop = True
                    break
            if stop:
                break

        return result

    def __g(self, char: str, key: int) -> str:
        return chr((ord(char) + 13 + key) % 26)

    def __xor(self, s1: str, s2: str) -> str:
        bin_s1 = ''.join(format(ord(i), '08b') for i in s1)
        bin_s2 = ''.join(format(ord(i), '08b') for i in s2)

        # Perform XOR and convert result back to string
        xor_result = ''.join(chr(
            int(bin_s1[i:i+8], 2) ^ int(bin_s2[i:i+8], 2)) for i in range(0, len(bin_s1), 8)
        )

        return xor_result

    def __half_slices(self, text: str) -> tuple[slice, slice]:
        return slice(None, len(text) // 2, None), slice(len(text) // 2, None, None)

