pesos = input('Cuantos pesos colombianos tienes? ')
pesos = float(pesos)
valor_dolar = 3875
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)

print('-------------------------------')
print('Tienes $' + dolares + ' dólares')
print('-------------------------------\n')

cordobas = input('Cuantos cordobas tienes? ')
cordobas = float(pesos)
valor_dolar = 36.10
dolares = cordobas / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)

print('-------------------------------')
print('Tienes $' + dolares + ' dólares')
print('-------------------------------')