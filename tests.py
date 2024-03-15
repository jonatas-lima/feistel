from feistel import feistel, decrypt

def test_basic():
    plain_text = "opa, david! tudo bem??"

    encrypted = feistel(plain_text)
    print('encrypted=', encrypted)
    decrypted = decrypt(encrypted)

    print('decrypted=', decrypted)
    assert plain_text == decrypted

def main():
    test_basic()

if __name__ == '__main__':
    main()
