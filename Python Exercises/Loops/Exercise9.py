# def run():
#     password = input('Enter the password: ')

#     x = 'password'

#     while True:
#         if password == x:
#             print('Correct password!')
#             break
#         else:
#             print('Enter the password again: ')
#             password = input('Enter the password: ')


def run():
    x = 'password'
    password = ''

    while password != x:
        password = input('Enter the password: ')
    print('Correct password!')
    


if __name__ == '__main__':
    run()