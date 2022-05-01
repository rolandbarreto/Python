def run():
    # numbers = [1,2,3,4,5,6,7,8,9,10]
    # for i in range(1, 11):
    #     print(numbers[-i], end=', ')

    numbers = [1,2,3,4,5,6,7,8,9,10]
    numbers.reverse()
    for i in numbers:
        print(i, end=', ')


if __name__ == '__main__':
    run()