def run():
    phrase = input('Enter a frase: ')
    letter = input('Enter a letter: ')

    c = 0

    for i in phrase:
        if i == letter:
            c += 1

    print('The letter ' + letter + ' appears ' + str(c) + ' times in the frase -> ' + phrase)


if __name__ == '__main__':
    run()