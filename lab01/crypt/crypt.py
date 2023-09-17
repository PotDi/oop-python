class FileCryptor:
    def __init__(self, key):
        self.key = key

    def open_file(self):
        pass

    def encrypt_file(self, input_file, output_file):
        with open(input_file, 'rb') as f_in:
            with open(output_file, 'wb') as f_out:
                byte = f_in.read(1)
                while byte:
                    encrypted_byte = bytes([byte[0] ^ self.key])
                    f_out.write(encrypted_byte)
                    byte = f_in.read(1)

    def decrypt_file(self, input_file, output_file):
        with open(input_file, 'rb') as f_in:
            with open(output_file, 'wb') as f_out:
                byte = f_in.read(1)
                while byte:
                    decrypted_byte = bytes([byte[0] ^ self.key])
                    f_out.write(decrypted_byte)
                    byte = f_in.read(1)
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


def parse_args():
    pass


