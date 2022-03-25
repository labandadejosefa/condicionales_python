# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda
if texto_1 > texto_2:
    print(f'"{texto_1}" es alfabéticamente mayor que "{texto_2}"')
elif texto_1 < texto_2:    
    print(f'"{texto_2}" es alfabéticamente mayor que "{texto_1}"')
else: 
    print(f'"{texto_1}" y "{texto_2}" son alfabéticamente equivalentes')    

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda
if len(texto_1) > len(texto_2):
    print(f'"{texto_1}" tiene mayor cantidad de letras que "{texto_2}"')
elif len(texto_1) < len(texto_2):    
    print(f'"{texto_2}" tiene mayor cantidad de letras que "{texto_1}"')
else:
    print(f'"{texto_1}" y "{texto_2}" tienen la misma cantidad de letras')    
 

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda
if copia_texto_1 == texto_1:
    print(f'La palabra "{copia_texto_1}" es igual a "{texto_1}"')

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda

if copia_texto_1 != texto_2:
    print(f'La palabra "{copia_texto_1}" es distinta a la palabra "{texto_2}"')

