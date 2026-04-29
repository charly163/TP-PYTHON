"""
Temas en el video:
* dic={}
* dic={'hola':'hello','azul':'blue'}
* dic['azul']='rojo'
* del(dic['azul'])
* auto= { 'marca': 'Ford',    'modelo': 'Mustang',    'año': 1964,    'precio': {'pesos': 5000, 'dolares': 600000}} #diccionario dentro de otro
lista_de_dicc=[]
* lista_de_dicc.append('auto')
* print(lista_de_dicc[0]['modelo'] )
—--------------------------------------------------------------------------------

"""

"""
### Ejercicio 1: Creación y modificación de un diccionario
1. Crea un diccionario `dic` con dos pares clave-valor: `'hola': 'hello'` y `'azul': 'blue'`.
2. Modifica el valor asociado a la clave `'azul'` para que ahora sea `'rojo'`.
3. Imprime el diccionario antes y después de la modificación.

"""

dic = {'hola': 'hello', 'azul': 'blue'}
print(dic)
dic['azul'] = 'rojo'
print(dic)

"""
### Ejercicio 2: Eliminación de un elemento en el diccionario
1. Crea un diccionario `colores` que tenga al menos tres pares clave-valor relacionados con colores.
2. Elimina el par con la clave `'azul'` usando `del()`.
3. Imprime el diccionario antes y después de la eliminación.
"""

colores = {'rojo': 'red', 'verde': 'green', 'azul': 'blue'}
print(colores)
del(colores['azul'])
print(colores)

"""
### Ejercicio 3: Diccionario dentro de otro diccionario
1. Crea un diccionario `auto` que contenga información sobre un vehículo con las claves `'marca'`, `'modelo'`, `'año'`, y un diccionario anidado para `'precio'` que incluya `'pesos'` y `'dolares'`.
2. Accede e imprime el valor del precio en dólares del auto.
3. Modifica el valor del precio en pesos y vuelve a imprimir el diccionario.

"""
auto = {'marca': 'Ford', 'modelo': 'Mustang', 'año': 1964, 'precio': {'pesos': 5000, 'dolares': 600000}}
print(auto['precio']['dolares'])
auto['precio']['pesos'] = 5500
print(auto)

"""
### Ejercicio 4: Lista de diccionarios
1. Crea una lista vacía llamada `lista_de_dicc`.
2. Agrega el diccionario `auto` (del ejercicio anterior) a la lista usando `append()`.
3. Accede e imprime el valor de la clave `'modelo'` del primer diccionario en la lista.
"""

lista_de_dicc = []
lista_de_dicc.append(auto)
print(lista_de_dicc[0]['modelo'])

"""
### Ejercicio 5: Lista de vehiculos
Codigo base: 
vehiculos = [
    {
        'marca': 'Ford',
        'modelo': 'Mustang',
        'año': 1964,
        'precio': {'pesos': 5000, 'dolares': 600000}
    },
    {
        'marca': 'Toyota',
        'modelo': 'Corolla',
        'año': 2020,
        'precio': {'pesos': 3500, 'dolares': 18000}
    },
    {
        'marca': 'Renault',
        'modelo': 'Clio',
        'año': 2015,
        'precio': {'pesos': 2800, 'dolares': 12000}
    }
]


# Validar si el precio en dólares supera cierto umbral
umbral = 20000


for auto in vehiculos:
    if auto['precio']['dolares'] > umbral:
        print(f"{auto['modelo']} supera el umbral de precio.")
    else:
        print(f"{auto['modelo']} está dentro del rango accesible.")


Consignas
1. Ejecutá el código y observá qué modelos superan el umbral de precio.
2. Cambiá el valor del umbral a 15000 y analizá cómo cambia la salida.
3. Agregá un nuevo vehículo a la lista con datos inventados.
4. Mostrá solo los modelos fabricados después del año 2018.
"""
lista_de_dicc.append({'marca': 'Chevrolet', 'modelo': 'Camaro', 'año': 2021, 'precio': {'pesos': 4500, 'dolares': 22000}})
print([auto['modelo'] for auto in lista_de_dicc if auto['año'] > 2018])