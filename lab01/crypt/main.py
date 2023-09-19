from crypt import FileCryptor

def main():
    input_file = 'input.bin'  # Имя входного файла
    encrypted_file = 'encrypted.bin'  # Имя зашифрованного файла
    decrypted_file = 'decrypted.bin'  # Имя дешифрованного файла
    key = 42  # Ключ для шифрования

    # Создание экземпляра класса
    file_encryptor_decryptor = FileCryptor(key)

    # Шифрование файла
    file_encryptor_decryptor.encrypt_file(input_file, encrypted_file)
    print('Файл успешно зашифрован.')

    # Дешифрование файла
    file_encryptor_decryptor.decrypt_file(encrypted_file, decrypted_file)
    print('Файл успешно дешифрован.')

if __name__ == '__main__':
    main()
