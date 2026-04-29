"""
Temas en el video:
if condición:
 verdadero
else:


if condición:
 verdadero
elif condición:
 verdadero
else:


if condicion1 or condición2:


if condicion1 and condicion2 



—-----------------------------------------------------------------------------------------------------------


 Ejercicio 1: Uso básico de `if` y `else`  
1. Escribe un programa que solicite al usuario ingresar un número.
2. Si el número es positivo, imprime "El número es positivo".
3. Si el número es negativo o igual a cero, imprime "El número es negativo o cero".
"""
numero = int(input("Ingrese un número: "))
if numero > 0:
    print("El número es positivo")
else:
    print("El número es negativo o cero")

"""
 Ejercicio 2: Uso de `if`, `elif` y `else`
1. Escribe un programa que solicite al usuario ingresar una calificación (de 0 a 100).
2. Si la calificación es mayor o igual a 90, imprime "A".
3. Si la calificación está entre 80 y 89, imprime "B".
4. Si la calificación está entre 70 y 79, imprime "C".
5. Si la calificación está por debajo de 70, imprime "F".
"""

calificacion = int(input("Ingrese una calificación (de 0 a 100): "))
if calificacion >= 90:
    print("A")
elif calificacion >= 80:
    print("B")
elif calificacion >= 70:
    print("C")
else:
    print("F")

"""
 Ejercicio 3: Uso de `if` con operadores lógicos `or`
1. Escribe un programa que solicite al usuario ingresar su edad.
2. Si la edad es menor de 18 **o** mayor de 65, imprime "No estás en el rango permitido para trabajar".
3. Si la edad está entre 18 y 65, imprime "Estás en el rango permitido para trabajar".

"""
edad = int(input("Ingrese su edad: "))
if edad < 18 or edad > 65:
    print("No estás en el rango permitido para trabajar")
else:
    print("Estás en el rango permitido para trabajar")

"""
 Ejercicio 4: Uso de `if` con operadores lógicos `and`
1. Escribe un programa que solicite al usuario ingresar dos números.
2. Si ambos números son positivos, imprime "Ambos números son positivos".
3. Si alguno de los dos números es negativo o cero, imprime "No ambos números son positivos".

"""
numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))
if numero1 > 0 and numero2 > 0:
    print("Ambos números son positivos")
else:
    print("No ambos números son positivos")


