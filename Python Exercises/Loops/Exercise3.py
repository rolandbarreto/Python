def run():
    number = int(input('Enter a number: '))

    for i in range(1, number + 1, 2):
        print(i, end=', ')


if __name__ == '__main__':
    run()