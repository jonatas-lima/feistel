class KeysGenerator:
    def __init__(self, initial_key: int):
        '''
        This class is used to generate the keys for the encryption and decryption

        :param initial_key: initial key to be used for the generation of the keys
        '''
        self.__private_key = initial_key

    def generate_keys(self, quantity=4) -> list[int]:
        '''
        This method is used to generate the keys for the encryption and decryption

        :param quantity: number of keys to be generated
        :return: list of keys
        '''
        keys = []
        for i in range(quantity):
            keys.append(self.__private_key << i)
        return list(map(lambda x: x % 127, keys))
