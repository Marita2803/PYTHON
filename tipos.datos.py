#esto es una lista
dias_semana = ['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo']

#imprimir los daos de una lista con un ofr
print("Días de la semana")
for dia in dias_semana:
    print(dia,'\n')

#esto es un diccioario de alumnos con sus calificaciones
calificaciones = {"Pepe":[2,4,5],"Juan":[3,4,4,],"Moisés":[4,3,5]}
print("Lista de alumnos")
for c in calificaciones:
    print(c,'\n')

print("Lista de alumnos con sus calificaciones")
for c in calificaciones:
    print(c,' : ',calificaciones[c],'\n')

print("Lista de alumnos y promedio de calificaciones")
for c in calificaciones:
    print(c,'\n')
    suma = 0
    for i in calificaciones[c]:
        suma +=i
    print('prom: {0}'.format((suma/len(calificaciones[c]))),'\n')

#tuplas, semejante a las listas pero inmutables
print('Meses del año','\n')
meses = ('enero','febrero','marzo','abril','mayo')
for mes in meses:
    print(mes,'\n')

#Otra lista, y los métodos de lista
precios = [4500,1200,3600,8000]
print(precios,'\n')
#agregar elementos a la lista
precios.append(900)
print(precios,'\n')
#quitar elemento según posición
precios.remove(1200)
print(precios,'\n')
#quitar el último elemento
print(precios.pop(),'\n')
print(precios,'\n')