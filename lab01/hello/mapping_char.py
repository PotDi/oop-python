def find_char():
    def get_text():
        user_text = list(input("Enter english text: "))
        return user_text

    original_text = get_text()
    vowels: str = "aeouiy"
    vowels_in_out = [char for char in original_text if char.lower() in
                     vowels]
    return vowels_in_out


found_vowels = find_char()
print(f"Find vowels: {found_vowels}")


# original_text = list(input("Enter english text: "))
# print(original_text)
# print(type(original_text))


def process_out(text: str, char: str):
    pass
