class FileCryptor:
    def __init__(self, key):
        self.key = key

    def encrypt_file(self, input_file: str, output_file: str):
        with open(input_file, 'rb') as f_in:
            with open(output_file, 'wb') as f_out:
                byte = f_in.read(1)
                while byte:
                    encrypted_byte = bytes([byte[0] ^ self.key])
                    f_out.write(encrypted_byte)
                    byte = f_in.read(1)

    def decrypt_file(self, input_file: str, output_file: str):
        with open(input_file, 'rb') as f_in:
            with open(output_file, 'wb') as f_out:
                byte = f_in.read(1)
                while byte:
                    decrypted_byte = bytes([byte[0] ^ self.key])
                    f_out.write(decrypted_byte)
                    byte = f_in.read(1)


