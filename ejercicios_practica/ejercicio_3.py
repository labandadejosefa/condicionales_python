# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese primero su nombre y luego su apellido
# Capture ambos datos e imprima su nombre completo
print('Ingrese por consola su/s nombre/s:')
nombre = str(input())

print('Ingrese por consola su/s apellido/s:')
apellido = str(input())

# Imprima su nombre completo
print('Su nombre completo es',nombre + ' ' + apellido)

# Almacenar su nombre completo en una variable
# nombre_completo = .....
nombre_completo= nombre + apellido

cant_letras = len(nombre_completo)
print('El total de caracteres de su nombre completo, es ',cant_letras)

# Imprimir la cantidad de letras que posee su nombre completo
# cantidad_letras = len(....)
