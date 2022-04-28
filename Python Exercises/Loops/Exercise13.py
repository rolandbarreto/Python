def run():
    while True:
        phrase = input('Enter a word, phrase or something: ')
        if phrase == 'exit':
            break
        print(phrase)


if __name__ == '__main__':
    run()