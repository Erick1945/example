#@author: Erick De La Rosa
promedio=[]
print("Calcula el promedio de las 5 calificaciones de 'N' numero de alumnos")
alumnos=input("Ingresa el numero de alumnos que avaluaras: ")
for i in range(0,int(alumnos),1):
  suma=0
  for j in range(0,5,1):
    nota=input("Ingresa la nota {j+1} del alumno {i+1}: ")
    suma+=nota
  promedio.append(suma/5)
  print()