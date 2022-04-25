def run():
    n = int(input('Enter a number: '))

    for i in range(n):
        print('*' * (i + 1))
        i += 1

if __name__ == '__main__':
    run()