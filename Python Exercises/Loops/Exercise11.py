def run():
    word = input('Enter a word: ')

    for i in range(len(word)-1, -1, -1):
        print(word[i])


if __name__ == '__main__':
    run()