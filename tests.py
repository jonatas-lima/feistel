from feistel import Feistel

def test_basic():
    f = Feistel(100)
    plain_text = "opa, david! tudo bem??"

    encrypted = f.encrypt(plain_text)
    print('encrypted=', encrypted)
    decrypted = f.decrypt(encrypted)

    print('decrypted=', decrypted)
    assert plain_text == decrypted

def main():
    test_basic()

if __name__ == '__main__':
    main()
