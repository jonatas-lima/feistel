class KeysGenerator:
    def __init__(self, initial_key: int):
        '''
        This class is used to generate the keys for the encryption and decryption

        :param initial_key: 64bit (8 bytes) key to be used for the encryption and decryption
        '''
        self.__private_key = initial_key
        self.__constant_64bit = 0b1111111111111111111111111111111111111111111111111111111111111111

    def __shift_bit_to_left(self, block: int) -> int:
        if block >= self.__constant_64bit:
            block -= self.__constant_64bit
            block = block << 1
            block += 1
        else:
            block = block << 1

        return block

    def __create_key_array(self) -> list[int]:
        '''
        This method is used to create the key array

        :return: list of keys
        '''
        keys = []
        block = self.__private_key

        for _ in range(0, 64):
            block = self.__shift_bit_to_left(block)
            keys.append(block)

        return keys

    def __break_hex_into_chunks(self, hex_value: int) -> list[str]:
        '''
        This method is used to break the hex value into chunks

        :param hex_value: hex value to be broken into chunks
        :return: list of chunks
        '''
        hex_string = hex(hex_value)[2:]
        hex_string = hex_string.zfill(16)

        return [hex_string[i:i + 2] for i in range(0, len(hex_string), 2)]

    def generate_keys(self) -> list[int]:
        '''
        This method is used to generate the keys for the encryption and decryption

        :return: list of keys
        '''
        row_keys = self.__create_key_array()
        keys = []

        counter = -1
        x = 0

        while x < 192 and counter < 16:
            i = x % 64
            byte_array = self.__break_hex_into_chunks(row_keys[i])

            if x % 12 == 0:
                keys.append([])
                counter += 1

            b = x % 4
            if counter % 2 == 1:
                b += 4

            hex_value = int(byte_array[b], 16)
            keys[counter].append(hex_value)
            x += 1

        return keys
