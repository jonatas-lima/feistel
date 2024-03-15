import random

BLOCK_SIZE = 8
ITERATIONS = 4
SEED = '1010101010101010'

random.seed(SEED)

def decrypt(encrypted_text: str, iterations: int = ITERATIONS) -> str:
    first_half_slice = slice(None, len(encrypted_text) // 2, None)
    second_half_slice = slice(len(encrypted_text) // 2, None, None)
    decoded = encrypted_text

    for _ in range(iterations):
        r0, l0 = decoded[first_half_slice], decoded[second_half_slice]
        e = fs(l0)
        l1, r1 = l0, xor_strings(r0, e)
        decoded = l1 + r1

    return decoded


def feistel(plain_text: str, iterations: int = ITERATIONS) -> str:
    first_half_slice = slice(None, len(plain_text) // 2, None)
    second_half_slice = slice(len(plain_text) // 2, None, None)
    encoded = plain_text

    for _ in range(iterations):
        l0, r0 = encoded[first_half_slice], encoded[second_half_slice]
        print(r0)
        e = fs(r0)
        print(e)
        l1, r1 = r0, xor_strings(l0, e)
        encoded = l1 + r1

    # print(encoded)
    return encoded


def fs(string: str, block_size: int = BLOCK_SIZE) -> str:
    return fs_alt(string, block_size)

    result = ''
    stop = False

    for i in range(0, len(string), block_size):
        for j in range(block_size):
            try:
                k = f(string[i+j])
                result += k
            except IndexError:
                stop = True
                break
        if stop:
            break

    return result

def fs_alt(string: str, block_size: int = BLOCK_SIZE) -> str:
    result = ''

    for i in range(0, len(string), block_size):
        s = string[i:i+block_size]
        list_s = list(s)
        random.seed(SEED)
        random.shuffle(list_s)
        result += ''.join(list_s)
        # diff = abs(len(s) - block_size)
        # for j in range(len(s) - diff):
        #     k = f(s[j])
        #     result += k


    return result

def f(char: str) -> str:
    return chr((ord(char) + 13) % 26)


def xor_strings(s1: str, s2: str) -> str:
    # Convert strings to binary
    bin_s1 = ''.join(format(ord(i), '08b') for i in s1)
    bin_s2 = ''.join(format(ord(i), '08b') for i in s2)

    # Perform XOR and convert result back to string
    xor_result = ''.join(chr(
        int(bin_s1[i:i+8], 2) ^ int(bin_s2[i:i+8], 2)) for i in range(0, len(bin_s1), 8)
    )

    return xor_result


def xor(x: str, y: str) -> str:
    hex_x = int(x, base=16)
    hex_y = int(y, base=16)
    res = hex(hex_x ^ hex_y)[2:]
    # diff = abs(len(res) - len(x)) * 4
    return res
