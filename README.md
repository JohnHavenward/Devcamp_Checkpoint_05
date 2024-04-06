# PREGUNTAS TEÓRICAS

[¿Qué es un condicional?](#condicionales)</br>
[¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?](#bucles)</br>
[¿Qué es una lista por comprensión en Python?](#listas-por-comprensión)</br>
[¿Qué es un argumento en Python?](#argumentos)</br>
[¿Qué es una función Lambda en Python?](#funciones-lambda)</br>
[¿Qué es un paquete pip?](#paquetes-pip)</br>
</br>



# CONDICIONALES

Los condicionales en python son una estructura de control básica capaz de evaluar una condición y ejecutar líneas de código u omitirlas en función de si esta se cumple o no se cumple.

Las condiciones evaluadas devuelven un valor booleano por lo que solo pueden ser `True` o `False`.

Para definir un condicional se debe usar la palabra clave `if` seguida de la expresión condicional a evaluar y el símbolo `:`. Finalmente se agrega el código a ejecutar en caso de cumplirse la condición, el cual debe estar correctamente indentado para evitar errores.

Vemos un ejemplo a continuación:


```python
x = 5
if x == 5:
    print("Es 5")
elif x == 6:
    print("Es 6")
elif x == 7:
    print("Es 7")
else:
    print("Es otro")
```

#### OPERADORES DE COMPARACIÓN

Expresión | Operación
:-------: | ---------
== | igual
!= | no Igual
< | menor que
<= | menor o igual que
\> | mayor que
\>= | mayor o igual que
</br>


### ELIF

En caso de que la primera condición no se cumpla, podemos agregar 

### ELSE

En caso de que no se cumpla ninguna de las condiciones anteriores po

### CONDICIONALES COMPUESTOS

#### OPERADORES LÓGICOS

Estos operadores evalúan dos condiciones y devuelven `True` en función de la operación representada. En el caso del operador `not` solo se evalúa una condición.

Expresión | Operación
:-------: | ---------
and | ambas condiciones se cumplen
or | al menos una de las dos condiciones se cumple
^ | una condición se cumple y la otra no 
not | la condición no se cumple


```python
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
```
### OPERADOR TERNARIO


</br></br></br>


**NOTA:**</br>
Para mayor información acerca del uso de condicionales en python consultar este [enlace](https://www.w3schools.com/python/python_conditions.asp).
</br></br></br></br></br>





# BUCLES




### ITERABLES E ITERADORES





### BUCLES FOR



### BUCLES WHILE



### BUCLES ANIDADOS




- Break y Continue
- Iterar cadenas
- for anidado xy
- for al revés
- Iterando cadena al revés. Haciendo uso de `[::-1]` se puede iterar la lista desde el último al primer elemento.

```python
texto = "Python"
for i in texto[::-1]:
    print(i) #n,o,h,t,y,P
```


</br></br></br>


**NOTA:**</br>
Para mayor información acerca del uso de bucles `for` en python consultar este [enlace](https://www.w3schools.com/python/python_for_loops.asp).

Para mayor información acerca del uso de bucles `while` en python consultar este [enlace](https://www.w3schools.com/python/python_while_loops.asp).
</br></br></br></br></br>





# LISTAS POR COMPRENSIÓN

Las listas de comprensión son una forma abreviada de de crear una lista a partir de otra modificando los elementos de esta y pudiendo comprobar la condición deseada para cada uno de ellos.

Las comprensiones de listas, sets o diccionarios son una herramienta muy útil para hacer que nuestro código resulte más compacto y fácil de leer. Siempre que tengamos una colección iterable que queramos modificar, son una buena opción para evitar tener que escribir bucles for.

Nos permiten hacer todo ello en una sola línea de código tal como vemos en el siguiente ejemplo, en el cual 

###### Ejemplo de uso
```python
# ejemplo
```
En caso de no usar una lista por comprensión el código es más largo y no resulta tan fácil de leer a simple vista. Vemos a continuación un bloque de código equivalente.

###### Código equivalente
```python
cuadrados = []
for i in range(5):
    cuadrados.append(i**2)
#[0, 1, 4, 9, 16]
```
</br>



### SINTAXIS

La sintaxis de una lista por comprensión es la que vemos a continuación

```python
lista_nueva = [expresión for elemento in iterable if condición]
```
</br>

#### *Expresión*

Es la expresión que se ejecuta cuando el elemento iterado cumple la condición. Esta expresión también puede ser una llamada a una función y no tiene por qué guardar relación con el elemento en cuestión, pudiendo ser una palabra o valor concreto por ejemplo.


```python
def eleva_al_2(i):
    return i**2

cuadrados = [eleva_al_2(i) for i in range(5)]
#[0, 1, 4, 9, 16]
```
</br>


#### *Lista nueva*

Es la nueva lista que se crea. La lista inicial no se ve alterada.
</br></br>


#### *Iterable*

Es la lista de la que se parte. pero también puede ser cualquier objeto iterable como una tupla, un set o un rango.
 

```python
new_list = [x.upper() for x in fruits]
```
</br>


#### *Condición*

La condición es opcional y puede ser omitida en la lista de comprensión. En tal caso la expresión es ejecutada para todos los elementos del objeto iterable.

###### Ejemplo
```python
frase = "El perro de san roque no tiene rabo"
erres = [i for i in frase if i == 'r']
#['r', 'r', 'r', 'r']
```



</br></br></br>


**NOTA:**</br>
Para mayor información acerca del uso de listas de comprensión en python consultar este [enlace](https://www.w3schools.com/python/python_lists_comprehension.asp).
</br></br></br></br></br>





# ARGUMENTOS

Los argumentos son la información que una función necesita para poder ejecutarse. A ser llamada esta 


### ARGUMENTOS Y PARÁMETROS

Aunque ambos términos pueden emplearse indistintamente cada uno tiene un significado estricto.

- Los **argumentos** son los valores que se pasan a la función cuando esta es llamada
- Los **parámetros** son las variables presentes en la definición de la función y que posteriormente toman los valores de los argumentos pasados

### NÚMERO DE ARGUMENTOS

</br>

### VALORES POR DEFECTO

Es posible tener argumentos con valor asignado por defecto.

```python
(lambda a, b, c=3: a + b + c)(1, 2) # 6
```
</br>


### ARGUMENTOS CON NOMBRE

También se pueden pasar los parámetros indicando su nombre.

```python
(lambda a, b, c: a + b + c)(a=1, b=2, c=3) # 6
```
</br>


### USO DE &nbsp;`*args`

Al igual que en las funciones se puede tener un número variable de argumentos haciendo uso de *, lo conocido como tuple unpacking.

```python
(lambda *args: sum(args))(1, 2, 3) # 6
```
</br>


### USO DE &nbsp;`**kwargs`

Y si tenemos los parámetros de entrada almacenados en forma de key y value como si fuera un diccionario, también es posible llamar a la función.

```python
(lambda **kwargs: sum(kwargs.values()))(a=1, b=2, c=3) # 6
```
</br>


### USO COMBINADO

```python
def funcion(a, b, *args, **kwargs):
    print("a =", a)
    print("b =", b)
    for arg in args:
        print("args =", arg)
    for key, value in kwargs.items():
        print(key, "=", value)

funcion(10, 20, 1, 2, 3, 4, x="Hola", y="Que", z="Tal")
#Salida
#a = 10
#b = 20
#args = 1
#args = 2
#args = 3
#args = 4
#x = Hola
#y = Que
#z = Tal
```






</br></br></br>


**NOTA:**</br>
Para mayor información acerca del uso de argumentos en python consultar este [enlace](https://www.w3schools.com/python/gloss_python_function_arguments.asp).
</br></br></br></br></br>





# FUNCIONES LAMBDA

Las funciones lambda, también llamadas anónimas, son una forma abreviada de definir una función que normalmente ocupan una única línea de código.

Deben ser asociadas a un variable para poder ser llamadas posteriormente

Para su definición se usa la palabra clave `lambda` y debe ser asociada a una variable.

Su principal limitación frente a una función normal de python es que solo pueden evaluar una única expresión. Pese a ello, las funciones lambda también pueden aceptar cualquier número de argumentos e igualmente permiten:

- dar un valor por defecto a los argumentos
- poder pasar los argumentos especificando su nombre  
- el uso de `*args` (*argument unpacking*)
- el uso de `**kwargs` (*keyword arguments*)



En el caso de las funciones lambda se omite el paso de tener que nombrar la función en su definición, por lo que para poder ser llamada posteriormente debe estar asociada a una variable. Al llamar a la variable debemos pasar los argumentos como en el caso de una función normal.


```python
suma = lambda a, b : a + b

print(suma(4, 3)) #7
```
</br>

En el ejemplo siguiente se muestra un función normal de python equivalente en su función

```python
def suma(a, b):
    return a + b
    
print(suma(4, 3)) #7
```
</br>




## SINTAXIS

```python
variable = lambda argumentos : expresión
```
</br>





Es posible declarar la función lambda y llamarla en la misma línea.

```python
mi_suma = (lambda a, b: a + b)(2, 4)
```







En el ejemplo siguiente la función lambda se combina con una función normal

```python
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) 
print(mytripler(11))
```


</br></br></br>


**NOTA:**</br>
Para mayor información acerca del uso de funciones Lambda en python consultar este [enlace](https://www.w3schools.com/python/python_lambda.asp).
</br></br></br></br></br>





# PAQUETES PIP













</br></br></br>


**NOTA:**</br>
Para mayor información acerca del uso de paquetes pip en python consultar este [enlace](https://www.w3schools.com/python/python_pip.asp).