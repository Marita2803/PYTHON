canasta = {}
continuar = True
while continuar:
    item = input('Introduce un artículo: ')
    precio = float(input('Introduce el precio de ' + item + ' : '))
    canasta[item] = precio
    #para continuar se debe escribir Si
    continuar = input('¿Quieres añadir artículos a la lista (si/no)? ') == "si"
coste = 0
print('Lista de la compra')
for item, precio in canasta.items():
    print(item, '\t', precio)
    coste += precio
print('Coste total: ', coste)