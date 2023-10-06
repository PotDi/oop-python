def write_file(file, data):
    file.write(data)


def open_file(input_file, mode):
    file = open(input_file, mode)
    return file


class FileCryptor:
    def __init__(self, key):
        self.__key = key

    def transform_bytes(self, byte):
        return bytes([byte[0] ^ self.__key])

    def read_file(self, file):
        byte = file.read(1)
        while byte:
            self.transform_bytes(byte)
            byte = file.read(1)
        return byte

    def encrypt_file(self, input_file: str, output_file: str):
        with open_file(input_file, 'rb') as f_in, open_file(output_file, 'wb') \
                as f_out:
            encrypted_byte = self.read_file(f_in)
            write_file(f_out, encrypted_byte)

    def decrypt_file(self, input_file: str, output_file: str):
        with open_file(input_file, 'rb') as f_in, open_file(output_file, 'wb') \
                as f_out:
            decrypted_byte = self.read_file(f_in)
            write_file(f_out, decrypted_byte)
