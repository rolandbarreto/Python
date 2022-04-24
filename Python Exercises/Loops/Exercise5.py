def run():
    amount = int(input('Enter - How much will you invest: $'))
    interest = float(input('Enter the anual interest: '))
    years = int(input('Enter for how many years: '))
    total_amount = 0

    for i in range(years):
        amount *= 1 + interest / 100
        print('Capital ' + str(i + 1) + ' years: '+ str(round(amount, 2)))
        total_amount += amount

    if i < years:
        print('Total amount: ' + str(round(total_amount, 2)) + ' at: ' + str(years) + ' years')

if __name__ == '__main__':
    run()
