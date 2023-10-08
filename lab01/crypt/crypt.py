def open_file(input_file, mode):
    try:
        file = open(input_file, mode)
    except IOError:
        return False
    return file


class FileCryptor:
    def __init__(self, key):
        self.__key = key

    def transform_bytes(self, byte):
        return bytes([byte[0] ^ self.__key])

    def encrypt_file(self, input_file: str, output_file: str):
        with open_file(input_file, 'rb') as f_in, open_file(output_file, 'wb') \
                as f_out:
            byte = f_in.read(1)
            while byte:
                encrypted_byte = self.transform_bytes(byte)
                f_out.write(encrypted_byte)
                byte = f_in.read(1)

    def decrypt_file(self, input_file: str, output_file: str):
        with open_file(input_file, 'rb') as f_in, open_file(output_file, 'wb') \
                as f_out:
            byte = f_in.read(1)
            while byte:
                decrypted_byte = self.transform_bytes(byte)
                f_out.write(decrypted_byte)
                byte = f_in.read(1)
