def conversor(divisa, valor_dolar):
    moneda = input('Cuantos ' + divisa + ' tienes? ')
    moneda = float(moneda)
    dolares = moneda / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)

    print('-------------------------------')
    print('Tienes $' + dolares + ' dólares')
    print('-------------------------------\n')

menu = """
Bienvenidos al conversor de monedas 💵

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos
4 - Cordobas nicaraguenses

Elige una opcion: """ 

opcion = int(input(menu))

if opcion == 1:
    conversor('pesos colombianos', 3875)
elif opcion == 2:
    conversor('pesos argentinos', 65)
elif opcion == 3:
    conversor('pesos mexicanos', 24)
elif opcion == 4:
    conversor('cordobas nicaraguenses', 36.10)
else:
    print('Ingresa una opcion correcta!')

