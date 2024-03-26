from keys import KeysGenerator

BLOCK_SIZE = 8
ITERATIONS = 4


class Feistel:
    def __init__(
        self,
        secret_key_path: str,
        iterations: int = ITERATIONS,
        block_size: int = BLOCK_SIZE,
    ) -> None:
        self.__iterations = iterations
        self.__block_size = block_size
        self.__padding_character = "#"

        kg = KeysGenerator(secret_key_path)
        self.__keys = kg.generate_keys(quantity=iterations)

    def __pad_message_to_8_bytes(self, message: str):
        return message + self.__padding_character * (self.__block_size - len(message) % self.__block_size)

    def __unpad_message(self, message: str):
        return message.rstrip(self.__padding_character)

    def encrypt(self, plain_text: str) -> str:
        padded_message = self.__pad_message_to_8_bytes(plain_text)

        first_half_slice, second_half_slice = self.__half_slices(padded_message)
        left, right = (
            padded_message[first_half_slice],
            padded_message[second_half_slice],
        )

        for i in range(self.__iterations):
            right_prev = right
            right = self.__xor(left, self.__f(right, i))
            left = right_prev

        return left + right

    def decrypt(self, encrypted_text: str) -> str:
        first_half_slice, second_half_slice = self.__half_slices(encrypted_text)
        left, right = (
            encrypted_text[first_half_slice],
            encrypted_text[second_half_slice],
        )

        for i in range(self.__iterations - 1, -1, -1):
            left_prev = left
            left = self.__xor(right, self.__f(left, i))
            right = left_prev

        concatenated = left + right

        return self.__unpad_message(concatenated)

    def __f(self, text: str, round: int) -> str:
        key = self.__keys[round]
        result = ""
        stop = False

        for i in range(0, len(text), self.__block_size):
            for j in range(self.__block_size):
                try:
                    k = self.__g(text[i + j], key)
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
        bin_s1 = "".join(format(ord(i), f"0{self.__block_size}b") for i in s1)
        bin_s2 = "".join(format(ord(i), f"0{self.__block_size}b") for i in s2)

        # Perform XOR and convert result back to string
        xor_result = "".join(
            chr(int(bin_s1[i : i + self.__block_size], 2) ^ int(bin_s2[i : i + self.__block_size], 2))
            for i in range(0, len(bin_s1), self.__block_size)
        )

        return xor_result

    def __half_slices(self, text: str) -> tuple[slice, slice]:
        return slice(None, len(text) // 2, None), slice(len(text) // 2, None, None)
