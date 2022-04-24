def run():
    n = int(input('Enter a number: '))

    for i in range(n, -1, -1):
        print(i, end=', ')


if __name__ == '__main__':
    run()