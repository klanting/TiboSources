import random


def generate(AuthSet, n=30):
    char_set = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while True:
        auth = ""
        for i in range(n):
                char = str(random.choice(char_set))
                number = random.random() * 100
                if number > 50:
                    char = char.capitalize()

                auth += char

        if auth not in AuthSet:
            AuthSet.add(auth)
            break

    return auth, AuthSet
