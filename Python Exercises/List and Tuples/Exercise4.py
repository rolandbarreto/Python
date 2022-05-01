def run():
    awarded = []
    for i in range(6):
        awarded.append(int(input('Enter a winner number: ')))
    awarded.sort()
    print('the winner numbers are: ' + str(awarded))


if __name__ == '__main__':
    run()