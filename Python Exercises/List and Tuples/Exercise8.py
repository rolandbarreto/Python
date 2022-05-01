
def run():
    word = input('Enter a word: ')
    reversed_word = word
    word = list(word)
    reversed_word = list(reversed_word)
    reversed_word.reverse()

    if word == reversed_word:
        print('Palindrome')
    else:
        print('Not a palindrome word')


if __name__ == '__main__':
    run()