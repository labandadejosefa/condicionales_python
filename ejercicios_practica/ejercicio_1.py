# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Ingrese dos números cualesquiera y realice las sigueintes
# comparaciones entre ellos
numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))

# Compare cual de los dos números es mayor

if numero_1 > numero_2:
    print(f'El número {numero_1} es mayor que {numero_2}')
elif numero_1 < numero_2:
    print(f'El número {numero_2} es mayor que {numero_1}')
else:
    print(f'Los números ingresados son equivalentes')    

# Imprima en pantalla según corresponda

# Verifique si el numero_1 positivo, negativo o cero
# Imprima el resultado en cada caso
if numero_1 > 0:
    print(f'El número {numero_1} es positivo')
elif numero_1 < 0:
    print(f'El número {numero_1} es negativo')
else:
    print(f'El número ingresado es igual a cero')        


# Verifique si el numero_1 es mayor a 0 y menor a 100
# Imprima en pantalla si se cumple o no la condición
if 0 < numero_1 < 100:
    print(f'El número {numero_1} es mayor que 0 y menor que 100')

# Verifique si el numero_1 es menor a 10 o el numero_2
# es mayor a -2
# Imprima en pantalla si se cumple o no la condición
if numero_1 < 10  or numero_2 > -2:
    print(f'O bien el número {numero_1} es menor que 10; o bien el número {numero_2} es mayor que -2')
