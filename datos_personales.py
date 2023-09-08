persona = {}
continuar = True
while continuar:
    #puedes cargar cualquier dato sobre una persona en el formate clave_valor
    clave = input('¿Qué dato quieres introducir? ')
    valor = input(clave + ' : ')
    persona[clave] = valor
    print(persona)
    #Tienes que escribir Si para continuar, en cualquier otro caso es False
    continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si" or "si"