from crypt import FileCryptor
import argparse

def main():
    args = parse_args()
    # Создание экземпляра класса
    file_encryptor_decryptor = FileCryptor(args.key)
    # Шифрование файла
    file_encryptor_decryptor.encrypt_file(args.input_file,
                                          args.encrypted_file)
    print('Файл успешно зашифрован.')
    # Дешифрование файла
    file_encryptor_decryptor.decrypt_file(args.encrypted_file,
                                          args.decrypted_file)
    print('Файл успешно дешифрован.')


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str, help="Source file name")
    parser.add_argument("encrypted_file", type=str, help="Encrypted file "
                                                         "name")
    parser.add_argument("decrypted_file", type=str, help="Decrypted file "
                                                       "name")
    parser.add_argument("key", type=int)
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    main()
