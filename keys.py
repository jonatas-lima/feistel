class KeysGenerator:
    def __init__(self, filepath: str):
        """
        This class is used to generate the keys for the encryption and decryption

        :param initial_key: initial key to be used for the generation of the keys
        """
        with open(filepath, "r") as file:
            self.__private_key = self.__sum_chars(file.read())

    def __sum_chars(self, text: str) -> int:
        """
        This method is used to sum the characters of a string

        :param text: string to be summed
        :return: sum of the characters
        """
        return sum([ord(char) for char in text]) % 127

    def generate_keys(self, quantity=4) -> list[int]:
        """
        This method is used to generate the keys for the encryption and decryption

        :param quantity: number of keys to be generated
        :return: list of keys
        """
        keys = []
        for i in range(quantity):
            keys.append(self.__private_key << i)
        return list(map(lambda x: x % 127, keys))
