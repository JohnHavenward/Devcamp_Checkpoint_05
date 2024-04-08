#Cree un bucle For de Python.

print('Ejercicio 1:\n')
      
for num in range(0, 11):
  print(10 - num)



#Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.

print('\n\nEjercicio 2:\n')

def suma(a, b, c):
  return a + b + c

print(suma(4, 6, 9))



#Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.

print('\n\nEjercicio 3:\n')

total_suma = lambda a, b, c: a + b + c

print(total_suma(3, 7, 15))



# Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. *Sugerencia, si es necesario, utilice un bucle for in y el operador in.
# nombre = 'Enrique'
# lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

print('\n\nEjercicio 4:\n')

nombre = 'Enrique'

lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

if nombre in lista_nombre:
  print('El nombre está en la lista')  
else:
  print('El nombre no está en la lista')