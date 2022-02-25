def convert(value, mod):
    value = value % mod
    return value


def reverse_calculate(value, a, mod):
    while True:
        value += mod
        check_value = value
        count = 0

        while check_value >= a:

            if check_value == a:
                print(value, count+1)

            if check_value % a == 0:
                count += 1
                check_value = check_value / a
            else:
                check_value = 0


if __name__ == "__main__":
    """
    count = 0
    lst = []
    for i in range(101):
        a = 7**i % 7919
        if a == 6302:
            print(i)
            lst.append(i)
            count += 1

    print(count, lst)
    """
    a = 8**8
    print(convert(a, 15))


