materias = ["Matemáticas","Física","Química","Historia","Lengua"]
notas = []
#recorrer materias como materia
for materia in materias:
    calificacion = input("Qué nota has sacado en " + materia + "?")
    notas.append(calificacion)
for i in range(len(materias)):
    print('\n', "En " + materias[i] + " has sacado " + notas[i])
