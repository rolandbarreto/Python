import random

def password_generator():
    Uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    Lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    Symbols = ['!', '#', '@', '%', '^', '&', '*', '(', ')', '_', '+', '?', '>', '<', '"','{', '}','|']
    Numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    characters = Uppercase + Lowercase + Symbols + Numbers

    password = []

    for i in range(16):
        characters_random = random.choice(characters)
        password.append(characters_random)

    password = ''.join(password)
    return password

def run():
    password = password_generator()
    print('Tu nueva contraseña es: ' + password)

if __name__ == '__main__':
    run()