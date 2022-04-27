def run():
    n = int(input('Enter a positive number greater than 2: '))
    i = 2

    while n % i != 0:
        i += 1
        print(i)
    if i == n:
        print(str(n) + " es primo")
    else:
        print(str(n) + " no es primo")
    

if __name__ == '__main__':
    run()
