def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuantos pesos " + tipo_pesos + " tienes? ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")


menu = """
Bienvenido al menu de monedas
1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos
Elige una opcion: """

opcion = int(input(menu))


if opcion == 1:
    conversor("Colombianos", 3750)
elif opcion == 2:
    conversor("Argentinos", 60)
elif opcion == 3:
    conversor("Mexicanos", 25)
else:
    print("Escribe una opcion correcta")
