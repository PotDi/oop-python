import sys


def open_file(input_file, mode):
    try:
        file = open(input_file, mode)
    except IOError:
        print(u'Не удалось открыть файл')
        sys.exit(1)
    else:
        return file


def mix_bits(byte) -> bytes:
    mix_byte = 0
    mix_order = [7, 5, 0, 4, 6, 2, 1, 3]
    for i, mix_index in enumerate(mix_order):
        bit = byte[0] >> i & 1
        mix_bit = bit << mix_index
        mix_byte = mix_byte | mix_bit
    return mix_byte


def transform_file(input_file: str, output_file:str,
                   transform):
    with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        while bytes := f_in.read(1):
            byte = transform(bytes[0])
            f_out.write(byte.to_bytes(1, 'big'))


class FileCryptor:
    def __init__(self, key: int):
        self.__key = key

    def encrypt_file(self, input_file: str, output_file: str):
        transform_file(input_file, output_file, self.__encrypt_byte)

    def decrypt_file(self, input_file: str, output_file: str):
        transform_file(input_file, output_file, self.__decrypt_byte)

    def __encrypt_byte(self, byte: int) -> int:
        return byte ^ self.__key

    def __decrypt_byte(self, byte: int) -> int:
        return byte ^ self.__key
