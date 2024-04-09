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
cantidad_hojas = 12

if cantidad_hojas < 50:
    print("Quedan pocas hojas")
    
# Quedan pocas hojas
```
</br>

La condición a evaluar también puede ser una variable. Esta puede ser un número o incluso una cadena en cuyo caso solo el número `0` y una cadena vacía `""` serán interpretados como `False`, y cualquier otro valor será evaluado como `True`. Vemos un ejemplo de ello a continuación:

```python
lluvia = True

if lluvia:
    print("Está lloviendo")
    
# Está lloviendo
```
</br>


#### OPERADORES DE COMPARACIÓN

Existen varios tipos de operadores para poder comparar expresiones y se muestran en la siguiente tabla:

Símbolo | Operación
:-----: | ---------
== | igual
!= | no Igual
< | menor que
<= | menor o igual que
\> | mayor que
\>= | mayor o igual que
</br>

Podemos ver varios ejemplos a continuación:

```python
print("abc" == "ABC") #False

print("Entrar" != "Salir") #True

print(3 < 8) #True

print(7 <= 5) #False

print("a" > "z") #False

print(4 >= 4) #True
```
</br>


### ELIF

En caso de que la primera condición no se cumpla y deseemos agregar condiciones alternativas a evaluar podemos hacerlo mediante la palabra clave `elif`.

Se pueden añadir tantos bloques elif como se desee pero estos se evalúan en el orden en el que han sido definidos en el condicional y en ningún caso se ejecutará más de uno. El primero en cumplir la condición será el único ejecutado.


```python
porcentaje_carga = 43

if porcentaje_carga < 5:
    print("Queda muy poca batería")
elif porcentaje_carga < 25:
    print("Queda menos del 25% de la batería")
elif porcentaje_carga < 50:
    print("Queda menos del 50% de la batería")
elif porcentaje_carga < 75:
    print("Queda menos del 75% de la batería")

# Queda menos del 50% de la batería
```
</br>


### ELSE

Podemos agregar un bloque de código que se ejecute en caso de que no se cumpla ninguna de las condiciones anteriores. Para ello debemos hacer uso de la palabra clave `else` sin ninguna condición asociada.

Solo puede haber un bloque *else* en un condicional y siempre debe estar definido al final de este. Podemos ver un ejemplo a continuación:

```python
color_objeto = "morado"

if color_objeto == "azul":
    print("El objeto es azul")
elif color_objeto == "rojo":
    print("El objeto es rojo")
else:
    print("El objeto no es ni azul ni rojo")
    
# El objeto no es ni azul ni rojo
```
</br>


### OPERADORES LÓGICOS

Estos operadores evalúan dos condiciones y devuelven `True` en función de la operación representada. En el caso del operador `not` solo se evalúa una condición. Podemos ver en la tabla siguiente la operación realizada por cada uno:

Expresión | Operación
:-------: | ---------
and | ambas condiciones se cumplen
or | al menos una de las dos condiciones se cumple
^ | una condición se cumple y la otra no 
not | la condición no se cumple
</br>

A continuación se muestran algunos ejemplos de su uso

```python
print(True and True) #True
print(True and False) #False
print(False and False) #False

print(True or True) #True
print(True or False) #True
print(False or False) #False

print(True ^ True) #False
print(True ^ False) #True
print(False ^ False) #False

print(not True) #False
print(not False) #True
```
</br>

Podemos ver el uso del operador lógico `not` en el siguiente condicional:

```python
acceso_permitido = False

if not acceso_permitido:
    print("No puedes pasar")
    
# No puedes pasar
``` 
</br>


### CONDICIONALES COMPUESTOS

Los condicionales compuestos nos permiten evaluar múltiples condiciones a la vez. Para ello debemos usar operadores lógicos tal y como se observa en el siguiente ejemplo:

```python
primera_condicion = True
segunda_condicion = True
tercera_condicion = False

if primera_condicion and segunda_condicion and tercera_condicion:
    print("Se cumplen todas condiciones")
else:
    print("No se cumplen todas condiciones")
    
# No se cumplen todas condiciones
```
</br>

A continuación podemos ver otro ejemplo de condicional compuesto:

```python
altura_viajero = 120
edad_viajero = 9

if altura_viajero >= 130 or edad_viajero >= 8:
    print("El viajero puede montarse en la atracción")
else:
    print("El viajero no puede montarse en la atracción")
    
# El viajero puede montarse en la atracción
```
</br>


### OPERADOR TERNARIO

Mediante un operador ternario podemos definir una condición y el código a ejecutar cuando se cumple al igual que otro alternativo para cuando no se cumple. En resumen se trata de una expresión if-else escrita de forma abreviada en una sola línea. En un operador ternario Siempre se ejecuta uno de los dos códigos y su estructura es la siguiente:

```python
[código si se cumple] if [condición] else [código si no se cumple]
```
</br>

A continuación podemos ver un ejemplo de uso:

```python
edad_usuario = 27

print("El usuario es mayor de edad" if edad_usuario >= 18 else "El usuario es menor de edad")

#El usuario es mayor de edad
```
</br></br></br>


**NOTA:**</br>
Para mayor información acerca del uso de condicionales en python consultar este [enlace](https://www.w3schools.com/python/python_conditions.asp).
</br></br></br></br></br>





# BUCLES

Los bucles son estructuras que nos permiten modificar el flujo de ejecución del código repitiendo un bloque de código múltiples veces. A cada repetición se la denomina iteración.

Existen dos tipos de bucles en python:

- Bucles `for`: tienen un número definido de iteraciones
- Bucles `while`: no tienen un número definido de iteraciones

</br>


### BUCLES FOR

Los bucles *for* ejecutan el bloque de código una vez por cada elemento de un objeto iterable. Normalmente este suele ser una lista, una tupla, un diccionario, un set o incluso una cadena. La cantidad de iteraciones a realizar viene predefinida en este caso por la cantidad de elementos existentes dentro del objeto.

Para su definición debemos usar la palabra clave `for`, especificar el nombre que tomará el elemento en cada iteración, usar la palabra `in`, designar el objeto a iterar y finalmente emplear el símbolo `:`. A continuación se escribe el bloque de código a ejecutar correctamente indentado. Podemos ver su estructura en el siguiente esquema: 

```python
for [nombre elemento] in [objeto iterable]:
    [bloque de código]
```
</br>

Vemos un ejemplo de bucle *for* a continuación:

```python
lista_palabras = ["Atardecer", "Castillo", "Incienso"]

for palabra in lista_palabras:
    print(palabra)
    
#Atardecer
#Castillo
#Incienso
```
</br>

En el siguiente ejemplo se itera un rango de valores para ejecutar el código el número de veces deseado:

```python
for iterador in range(4):
    print(f"Esta iteración es la número {iterador + 1}")

#Esta iteración es la número 1
#Esta iteración es la número 2
#Esta iteración es la número 3
#Esta iteración es la número 4
```
</br>

Los bucles *for* también pueden iterar una cadena de caracteres ejecutando el código para cada letra. Podemos ver un ejemplo de ello a continuación:

```python
lista_letras = []

for letra in "PYTHON":
    lista_letras.append(letra.lower())

print(lista_letras)

#['p', 'y', 't', 'h', 'o', 'n']
```
</br>


### BUCLES WHILE

Con los bucles *while* podemos ejecutar un bloque de código un número indeterminado de veces siempre y cuando se cumpla una condición previamente definida. Esta condición es evaluada al comienzo de cada iteración y debemos asegurarnos de que en algún momento esta condición deje de cumplirse.

Para su definición empezamos con la palabra clave `while`, después escribimos la condición a evaluar y terminamos con el símbolo `:`. A continuación se debe especificar el bloque de código a ejecutar correctamente indentado. Podemos ver su estructura en el siguiente esquema: 

```python
while [condición]:
    [bloque de código]
```
</br>

Podemos ver un ejemplo de uso de un bucle *while* a continuación:

```python
semana = []

while len(semana) < 7:
    semana.append(f"D{len(semana) + 1}")

print(semana)

#['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7']
```
</br>

Si durante la ejecución del bucle la condición no se deja de cumplir en alguna de las iteraciones, se producirá un bucle infinito y no podrá continuar ejecutándose el resto del programa.

Es por ello que en esta clase de bucles suele ser frecuente la definición de una variable de indexado. Esta se define antes del bucle y nos permite partir de un valor de referencia para poder controlar las iteraciones realizadas. Vemos un ejemplo de ello a continuación:

```python
i = 0

while i < 50:
    i += 1
  
print(i)

#50
```
</br>


### BUCLES ANIDADOS

Podemos definir un bucle dentro de otro bucle. En este tipo de estructuras el bucle interno se ejecuta una vez por cada iteración del bucle externo, tal y como se observa en el siguiente ejemplo:

```python
filas = [*range(1,5)]
columnas = [*range(1,6)] 

for fila in filas:
    fila_actual = []
    for columna in columnas:
        fila_actual.append(columna + fila)  
    print(fila_actual)
    
#[2, 3, 4, 5, 6]
#[3, 4, 5, 6, 7]
#[4, 5, 6, 7, 8]
#[5, 6, 7, 8, 9]
```
</br>


### DECLARACIONES BREAK Y CONTINUE

Se puede alterar el flujo normal de un bucle sin importar el punto de ejecución en el que se encuentre. Existen dos formas diferentes:

- hacer que el bucle finalice directamente
- hacer que la iteración actual finalice directamente y comience la siguiente
</br>

La palabra clave `break` rompe el flujo del bucle y este finaliza directamente. Podemos ver su uso en el ejemplo siguiente:

```python
iteraciones = 0

while iteraciones < 10:
    if iteraciones == 5:
        break
    iteraciones += 1
   
print(iteraciones)

#5
```
</br>

La palabra clave `continue` termina de ejecutar la iteración actual y comienza directamente la siguiente. Se muestra un ejemplo de su uso a continuación:

```python
lista_frutas = ["manzana", "plátano", "fresa", "piña",]
for fruta in lista_frutas:
    if fruta == "plátano":
        continue
    print(fruta)
    
#manzana
#fresa
#piña
```
</br>


### BLOQUE ELSE

Ambos tipos de bucle permiten definir un bloque de código a ejecutar tras su finalización. En el caso del bucle *for* cuando todos los elementos han sido iterados y en el caso del bucle *while* cuando la condición deja de cumplirse. Este bloque de código se define con la palabra clave `else` tal y como vemos en el siguiente ejemplo:

```python
cuenta = 0

for x in range(1000):
    cuenta += 1
else:
    print(f"Bucle finalizado tras {cuenta} iteraciones")
  
#Bucle finalizado tras 1000 iteraciones  
```
</br>

Cabe destacar que si el bucle finaliza tras la ejecución de la sentencia `break` este bloque de código final no se ejecutará. Podemos ver un ejemplo de ello a continuación:

```python
joyas = ["esmeralda", "rubí", "diamante", "zafiro", "amatista"]

while joyas:
    if joyas.pop() == "diamante":
        break
else:
    joyas = []

print(joyas)
  
#['esmeralda', 'rubí'] 
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

```python
lista_numeros = [7, 13, 10, 15, 8, 51, 32]

numeros_impares = [numero for numero in lista_numeros if numero % 2 != 0]

print(numeros_impares)

# [7, 13, 15, 51]
```
</br>

En caso de no usar una lista por comprensión el código es más largo y no resulta tan fácil de leer a simple vista. Vemos a continuación un bloque de código equivalente.

```python
lista_numeros = [7, 13, 10, 15, 8, 51, 32]
numeros_impares = []

for numero in lista_numeros:
    if numero % 2 != 0:
        numeros_impares.append(numero)

print(numeros_impares)

# [7, 13, 15, 51]
```
</br>


### SINTAXIS

La sintaxis de una lista por comprensión es la que vemos a continuación

```python
lista_nueva = [expresión for elemento in iterable if condición]
```
</br>

A continuación se explica uno a uno cada uno de los componentes de una lista por comprensión.
</br></br>


#### *Lista nueva*

Es la nueva lista que se crea. La lista inicial no se ve alterada.
</br></br>


#### *Iterable*

Es la lista de la que se parte pero también puede ser cualquier objeto iterable como una tupla, un set o un rango.

En el siguiente ejemplo vemos el uso de un rango.

```python
siete_numeros = [num for num in range(1,8)]

print(siete_numeros)

# [1, 2, 3, 4, 5, 6, 7]
```
</br>


#### *Elemento*

Es el nombre dado al elemento en cada iteración.
</br></br>


#### *Expresión*

Es la expresión que se ejecuta cuando el elemento iterado cumple la condición. Esta no tiene por qué guardar relación con el elemento iterado, pudiendo ser una palabra o valor concreto por ejemplo.

La expresión también puede ser una llamada a una función como en el siguiente ejemplo:

```python
lista_numeros = [0, 1, 2, 3, 4, 5]

def eleva_al_cubo(n):
    return n**3

numeros_cubos = [eleva_al_cubo(numero) for numero in lista_numeros if numero != 0]

print(numeros_cubos)

# [1, 8, 27, 64, 125]
```
</br>


#### *Condición*

La condición es opcional y puede ser omitida en la lista de comprensión. En tal caso la expresión es ejecutada para todos los elementos del objeto iterable.

```python
mi_frase = "La casa es roja"

lista_letras = [letra.upper() for letra in mi_frase if letra != ' ']

print(lista_letras)

# ['L', 'A', 'C', 'A', 'S', 'A', 'E', 'S', 'R', 'O', 'J', 'A']
```
</br></br></br>


**NOTA:**</br>
Para mayor información acerca del uso de listas de comprensión en python consultar este [enlace](https://www.w3schools.com/python/python_lists_comprehension.asp).
</br></br></br></br></br>





# ARGUMENTOS

Los argumentos son la información que es pasada a una función para esta poder ser ejecutada. En la llamada los argumentos son especificados junto al nombre de la función dentro de paréntesis y separados por comas. En el caso de no pasar ningún argumento los paréntesis se dejan vacíos.  

Vemos un ejemplo de uso de argumentos al llamar a una función en el ejemplo siguiente:

```python
def multiplicar(a, b, c):
    return a * b * c

print(multiplicar(10, 3, 4))

#120
```
</br>


### ARGUMENTOS Y PARÁMETROS

Aunque ambos términos pueden emplearse indistintamente cada uno tiene un significado estricto.

- Los **argumentos** son los valores que se pasan a la función cuando esta es llamada
- Los **parámetros** son las variables presentes en la definición de la función y que posteriormente toman los valores de los argumentos pasados

</br>


### NÚMERO Y ORDEN DE ARGUMENTOS

La cantidad de argumentos especificada en la llamada de la función siempre debe coincidir con la cantidad que esta espera. Igualmente hay que tener en cuenta que el orden de los argumentos debe ser el mismo en el que han sido definidos los parámetros.

Vemos un ejemplo a continuación:
```python
def mi_funcion(primer_parametro, segundo_parametro, tercer_parametro):
    print(f"{primer_parametro}, {segundo_parametro} y {tercer_parametro}")

mi_funcion("primer_argumento", "segundo_argumento", "tercer_argumento")

#primer_argumento, segundo_argumento y tercer_argumento
```
</br>


### VALORES POR DEFECTO

Es posible tener parámetros definidos con un valor por defecto en la función. En ese caso si un argumento no es pasado a la función el parámetro toma el valor asignado por defecto tal y como ocurre en el siguiente ejemplo:

```python
def numero_telefono(numero, prefijo = "+34"):
    print(f"El teléfono es el ({prefijo}){numero}")

numero_telefono(789456123)

#El teléfono es el (+34)789456123
```
</br>


### ARGUMENTOS CON NOMBRE

En el caso de conocer el nombre de cada parámetro de la función podemos especificar cada argumento mediante su nombre. En este caso el orden en el que pasamos los argumentos a la función no importa. Se muestra un ejemplo a continuación: 

```python
def describir_objeto(tamaño, forma, color):
    print(f"El objeto es {tamaño}, {forma} y de color {color}")

describir_objeto(forma = "cuadrado", color = "naranja", tamaño = "grande")

#El objeto es grande, cuadrado y de color naranja
```
</br>


### ARGUMENTOS ARBITRARIOS

La función puede tener definido un parámetro mediante la expresión `*args`. Esto indica que espera un número indeterminado de argumentos y al pasarlos a la función son tratados como una tupla. Es por ello que pueden ser iterados dentro del código de la función. Podemos ver un ejemplo de ello a continuación:

```python
def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(suma(5, 3, 2, 7))

#Salida 17
```
</br>

El uso del nombre `*args` es una convención, pudiendo ser usado cualquier otro siempre que este comience con el símbolo `*`. 
</br></br>


### ARGUMENTOS *KEYWORD* ARBITRARIOS

La función puede tener definido un parámetro mediante la expresión `**kwargs`. Esto indica que espera un número indeterminado de argumentos del tipo clave-valor. Al pasarlos a la función estos son tratados como un diccionario tal y como vemos en el siguiente ejemplo:

```python
def duplicar_valores(**kwargs):
    resultados = []
    for key, value in kwargs.items():
        resultados.append(f"{key} = {value * 2}")
    return resultados
    
print(duplicar_valores(x = 6, y = 10, z = -3))

#['x = 12', 'y = 20', 'z = -6']
```
</br>

El uso del nombre `**kwargs` es una convención, pudiendo ser usado cualquier otro siempre que este comience con `**`. 
</br></br>


### USO COMBINADO DE TIPOS DE ARGUMENTOS

Es posible mezclar argumentos normales con `*args` y `**kwargs` dentro de la misma función. Lo único que hay que tener en cuenta es que siempre deben ser definidos en el siguiente orden:

- Primero argumentos normales
- Después los argumentos `*args`
- Y por último los argumentos `**kwargs`

</br>

Vemos un ejemplo del uso combinado de tipos de argumentos a continuación:

```python
def funcion_combinada(doble, triple, *animales, **colores):
    print(doble * 2)
    print(triple * 3)
    for animal in animales:
        print(animal)
    for color in colores.values():
        print("color " + color)

funcion_combinada(10, 20, "perro", "gato", "cerdo", "vaca", color_1 ="rojo", color_2="verde", color_3 = "azul")

#20
#60
#perro
#gato
#cerdo
#vaca
#color rojo
#color verde
#color azul
```
</br></br></br>


**NOTA:**</br>
Para mayor información acerca del uso de argumentos en python consultar este [enlace](https://www.w3schools.com/python/gloss_python_function_arguments.asp).
</br></br></br></br></br>





# FUNCIONES LAMBDA

Las funciones lambda, también llamadas anónimas, son una forma abreviada de definir una función que normalmente ocupan una única línea de código. Para su definición se usa la palabra clave `lambda` tal y como vemos en el siguiente ejemplo:

```python
producto = lambda a, b, c : a * b * c

print(producto(4, 3, 6)) #72
```
</br>


En el ejemplo siguiente se muestra el código equivalente usando una función normal de python:

```python
def producto(a, b, c):
    return a * b * c
    
print(producto(4, 3, 6)) #72
```
</br>


La sintaxis de una función lambda es la siguiente:

```python
variable = lambda argumentos : expresión
```
</br>


En el caso de las funciones lambda se omite el paso de ser nombradas, por lo que para poder ser llamadas posteriormente deben estar siempre asociadas a una variable. Al llamar a esta variable debemos pasar los argumentos como si se tratase de  función normal de python.

Su principal limitación frente a una función normal de python es que solo pueden evaluar una única expresión. Pese a ello, las funciones lambda también pueden aceptar cualquier número de argumentos e igualmente permiten:

- dar un valor por defecto a los argumentos
- poder pasar los argumentos especificando su nombre  
- el uso de `*args` (*argument unpacking*)
- el uso de `**kwargs` (*keyword arguments*)

</br>


En el siguiente ejemplo la función lambda acepta un número indeterminado de argumentos mediante el uso de `*args` y además podemos comprobar que es posible declarar la función y llamarla en la misma línea:

```python
print((lambda *args: sum(args))(10, 3)) #13

print((lambda *args: sum(args))(8, 9, 4)) #21
```
</br>


Es posible combinar ambos tipos de funciones. En el ejemplo siguiente una función lambda es retornada al llamar a una función normal de python:

```python
def potencia(n):
  return lambda a : a ** n

elevar_al_cuadrado = potencia(2)
elevar_al_cubo = potencia(3)

print(elevar_al_cuadrado(5)) #25

print(elevar_al_cubo(2)) #8
```
</br></br></br>


**NOTA:**</br>
Para mayor información acerca del uso de funciones Lambda en python consultar este [enlace](https://www.w3schools.com/python/python_lambda.asp).
</br></br></br></br></br>





# PAQUETES PIP

Para poder entender qué es un paquete PIP debemos entender primero los siguientes dos conceptos:

- Un paquete es un conjunto de archivos necesarios para un módulo python
- PIP es un sistema de gestor de paquetes para python

</br>


### MÓDULOS PYTHON

Un módulo es una librería de código python que podemos incluir en nuestro proyecto. Puede ser desde un solo fichero `.py` hasta un paquete de archivos. Estos módulos incluyen un conjunto de funciones, variables o clases que pueden aportarnos soluciones y nos ahorren así trabajo y tiempo de desarrollo.

Algunos módulos existen dentro de python y los podemos importar directamente a nuestro proyecto. En en siguiente enlace a la documentación oficial podemos encontrar una lista completa:

- [Lista de módulos preinstalados en python](https://docs.python.org/3/py-modindex.html).
</br></br>

Sin embargo existe una cantidad mucho mayor de módulos creados por la comunidad de desarrolladores de python que también podemos incluir en nuestros proyectos. Son los llamados módulos externos y la principal diferencia es que estos deben ser instalados antes de poder ser importados. Podemos encontrar muchos de ellos en el siguiente enlace:

- [El Índice de paquetes de Python (PyPI)](https://pypi.org).
</br></br>


#### *Importar módulos*

Imaginemos que tenemos el siguiente archivo llamado `mi_modulo.py` y tiene las funciones `suma()` y `resta()` definidas en él:

```python
# mi_modulo.py
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b
```
</br>

Ese archivo esta localizado en la carpeta de nuestro proyecto y deseamos añadirlo al archivo en el que estamos trabajando. Para importar ese módulo y poder usar sus funciones debemos emplear la palabra clave `import` tal y como vemos a continuación:

```python
import mi_modulo

print(mi_modulo.suma(7, 2)) #9
print(mi_modulo.resta(10, 7)) #3
```
</br>


#### *Importar componentes*

Se puede importar directamente los componentes que nos interesen evitando así tener que incluir el nombre del módulo cada vez que hacemos uso del componente. Vemos un ejemplo a continuación:

```python
from mi_modulo import suma, resta

print(suma(7, 2)) #9
print(resta(10, 7)) #3
```
</br>

También podemos importar todos los componentes definidos dentro del módulo usando el símbolo `*` tal y como se muestra a continuación:

```python
from mi_modulo import *

print(suma(7, 2)) #9
print(resta(10, 7)) #3
```
</br>


#### *Renombrar módulos*

En ocasiones un módulo puede tener un nombre demasiado largo o darse el caso de que exista otro módulo con el mismo nombre. En ese tipo de situaciones tenemos la posibilidad de renombrar el módulo al importarlo a nuestro archivo y darle un nuevo nombre. Podemos ver un ejemplo de ello a continuación: 

```python
import mi_modulo as m

print(m.suma(7, 2)) #9
print(m.resta(10, 7)) #3
```
</br>


#### *Importar módulos en subcarpetas*

Imaginemos que el módulo a importar se encuentra dentro de una subcarpeta de nuestro proyecto tal y como se muestra en el siguiente esquema:

```terminal
.
├── ejemplo.py
├── carpeta
│   └── mi_modulo.py
```
</br>

En este caso debemos especificar la ruta del archivo separada por `.` junto al nombre del módulo tal y como se ve el el siguiente ejemplo:

```python
from carpeta.modulo import *
print(hola())
# Hola
```
</br>


### PIP

PIP es un gestor de paquetes de python que nos permite descargar e instalar módulos externos en nuestro sistema. Una vez instalados podremos incluir estos en nuestros proyectos. También nos permite llevar un control de las versiones de los paquetes instalados y poder actualizarlos.

Una vez hemos instalado PIP en nuestro sistema podemos usar el siguiente comando de la terminal para instalar el paquete deseado:

```console
pip install nombre_paquete
```
</br>

Para mostrar una lista completa de los paquetes PIP instados y sus respectivas versiones debemos usar el siguiente comando:

```console
pip list
```
</br>

Para desinstalar un paquete debemos usar el siguiente comando:

```console
pip uninstall nombre_paquete
```
</br>

Para actualizar un paquete debemos usar el siguiente comando:

```console
pip install --upgrade nombre_paquete
```
</br>


#### *pipenv*

La herramienta *pipenv* resulta muy útil ya que nos permite crear entornos de trabajo independientes para cada unos de nuestros proyectos. La principal ventaja es que esto nos permite hacer uso de diferentes versiones del mismo paquete en cada uno de ellos.
</br></br></br>


**NOTA:**</br>
Para mayor información acerca del uso de paquetes pip en python consultar este [enlace](https://www.w3schools.com/python/python_pip.asp).