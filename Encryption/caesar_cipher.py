def encrypt(string, value):
    new_string = ""

    for char in string:
        case = char.isupper()
        char = char.lower()
        i = ord(char)

        if 97 <= i <= 122:
            i += value

            if not i <= 122:
                i -= 26

            char = chr(i)
            if case:
                char = char.upper()

        new_string += char

    return new_string


def decrypt(string, value):
    new_string = ""

    for char in string:
        case = char.isupper()
        char = char.lower()
        i = ord(char)

        if 97 <= i <= 122:
            i -= value

            if not i >= 97:
                i += 26

            char = chr(i)
            if case:
                char = char.upper()

        new_string += char

    return new_string


if __name__ == '__main__':
    new = encrypt("basic testing", 1)
    new = decrypt(new, 1)
    print(new)
