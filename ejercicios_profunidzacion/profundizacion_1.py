# Tipos de variables [Python]
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
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio

num_1 = float(input('Ingrese un número real: '))
num_2 = float(input('Ingrese otro número real: '))

adic = num_1 + num_2
dife = num_1 - num_2
produ = num_1 * num_2
cociente = num_1 / num_2
expo = num_1 ** num_2

print('La suma de',num_1,'y',num_2, ', es',adic)
print('La resta de',num_1,'menos',num_2, ', es',dife)
print('El producto entre',num_1,'y',num_2, ', es',produ)
print('El cociente entre',num_1,'y',num_2, ', es',round(cociente,4))
print('El valor de ',num_1, 'elevado a la potencia',num_2, ', es',expo)
