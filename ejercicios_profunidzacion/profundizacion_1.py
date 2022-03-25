# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite por consola 2 números
Calcule la diferencia entre ellos e informe por pantalla
si el resultado es positivo, negativo o cero.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

num1 = int(input('Ingrese un número:\n'))
num2 = int(input('Ingrese otro número:\n'))

resta = num1 - num2

if resta == 0:
    print('Los números ingresados son idénticos. Su diferencia es igual a cero. ')
elif resta > 0:
    print(f'La diferencia entre {num1} y {num2} es un valor positivo, pues {num1} es mayor que {num2}.')
else:
    print(f'La diferencia entre {num1} y {num2} es un valor negativo, pues {num1} es menor que {num2}.')        
