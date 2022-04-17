menu = """
Bienvenidos al conversor de monedas 💵

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos
4 - Cordobas nicaraguenses

Elige una opcion: """ 

opcion = int(input(menu))

if opcion == 1:
    pesos = input('Cuantos pesos colombianos tienes? ')
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)

    print('-------------------------------')
    print('Tienes $' + dolares + ' dólares')
    print('-------------------------------\n')
elif opcion == 2:
    pesos = input('Cuantos pesos argentinos tienes? ')
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)

    print('-------------------------------')
    print('Tienes $' + dolares + ' dólares')
    print('-------------------------------\n')
elif opcion == 3:
    pesos = input('Cuantos pesos mexicanos tienes? ')
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)

    print('-------------------------------')
    print('Tienes $' + dolares + ' dólares')
    print('-------------------------------\n')
elif opcion == 4:
    cordobas = input('Cuantos cordobas tienes? ')
    cordobas = float(cordobas)
    valor_dolar = 36.10
    dolares = cordobas / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)

    print('-------------------------------')
    print('Tienes $' + dolares + ' dólares')
    print('-------------------------------')
else:
    print('Ingresa una opcion correcta!')

