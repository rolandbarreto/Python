def run():

    prices = [50, 75, 46, 22, 80, 65, 8]
    min = max = prices[0]

    print(min)
    print(max)

    for i in prices:
        if i < min:
            min = i
        elif i > max:
            max = i
    
    print('the lower is: ' + str(min))
    print('The higher is: ' + str(max))


if __name__ == '__main__':
    run()