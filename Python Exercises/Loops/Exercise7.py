from re import I


def run():
    x = int(input('Enter the multiplication table to calculate: '))

    for i in range(12 + 1):
        print(str(x) + ' x ' + str(i) + ' = ' + str(i * x))
        i += 1


if __name__ == '__main__':
    run()