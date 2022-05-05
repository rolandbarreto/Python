def run():
    # word = input('Enter a word: ')
    # word = list(word)

    # a = 0
    # e = 0
    # i = 0
    # o = 0
    # u = 0

    # for w in word:
    #     if w == 'a':
    #         a += 1
    #     elif w == 'e':
    #         e += 1
    #     elif w == 'i':
    #         i += 1
    #     elif w == 'o':
    #         o += 1
    #     elif w == 'u':
    #         u += 1
    
    # print('a = ' + str(a))
    # print('e = ' + str(e))
    # print('i = ' + str(i))
    # print('o = ' + str(o))
    # print('u = ' + str(u))

    word = input("Enter a word: ")
    vowels = ['a', 'e', 'i', 'o', 'u']

    for vowel in vowels:
        times = 0
        for letter in word:
            if letter == vowel:
                times += 1
        print("The vowel " + vowel + ' appears ' + str(times) + ' times')


if __name__ == '__main__':
    run()