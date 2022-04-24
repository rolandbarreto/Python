def run():
    age = int(input('Enter your age: '))

    for i in range(age):
        print(i + 1)
        i += 1

if __name__ == '__main__':
    run()