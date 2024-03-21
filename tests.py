from feistel import Feistel


def test_basic():
    f = Feistel("./secrets/secret_key")
    plain_text = "opa, david! tudo bem?"

    encrypted = f.encrypt(plain_text)
    print("encrypted=", encrypted)
    decrypted = f.decrypt(encrypted)

    print("decrypted=", decrypted)
    assert plain_text == decrypted


def test_with_different_keys():
    f1 = Feistel("./secrets/secret_key")
    plain_text = "opa, david! tudo bem?"

    encrypted_1 = f1.encrypt(plain_text)
    print("encrypted_1=", encrypted_1)
    decrypted_1 = f1.decrypt(encrypted_1)

    print("decrypted_1=", decrypted_1)
    assert plain_text == decrypted_1

    f = Feistel("./secrets/alt_secret_key")

    encrypted_2 = f.encrypt(plain_text)
    print("encrypted_2=", encrypted_2)
    decrypted_2 = f.decrypt(encrypted_2)

    print("decrypted_2=", decrypted_2)
    assert plain_text == decrypted_2 == decrypted_1

    assert encrypted_1 != encrypted_2

def main():
    test_basic()
    print('-'*50)
    test_with_different_keys()


if __name__ == "__main__":
    main()
