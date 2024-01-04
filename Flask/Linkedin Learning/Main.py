#El curso empieza por mostrar las listas, enseña que en lugar de poner todo lo siguiente
#es mas facil solo hacerlo una lista
# ciudad1 = 'Mexico'
# ciudad2 = 'Aguas'
# ciudad3 = 'Micho'
# ciudad4 = 'Colima'

Ciudades = [
    'Mexico',
    'Aguas',
    'Micho',
    'Colima'
    ]

#Llegamos a la parte de diccionario que se refiere mas que nada a agrupar listas que esten
#llenas de variables, y nos pone el siguiente ejemplo
#Animales
# pez = 'Pez espapda'
# anfibio = 'Rana'
# Reptil = 'Tortuga'
# ave = 'Avestruz'
# mamifero = 'Elefante'

Animales = {
    'pez': 'Pez espapda',
    'anfibio': 'Rana',
    'Reptil': 'Tortuga',
    'ave': 'Avestruz',
    'mamifero': 'Elefante'
}

#Para trabajar con colecciones es tan sencillo como solo seleccionar su numero asigando
print(Ciudades[2])
print(Animales['pez'])

#ITERACIONES

ingredientes = [
    'Sal',
    'Pimienta',
    'Cebollino',
    'Chile'
]
for ingrediente in ingredientes:
    print(ingrediente)
print('Asi me gustan las tortillas')


print('Contando de 5 en 5 hasta 100')
i = 5
while i <= 100:
    print(i)
    i += 5
print('Cuenta completa')

import Modulos

Modulos.mult(10,5)


#Strings
valor = input('Ingresa un numero')
print(valor + ' Es mi numero xd')
print('Cuando se multiplica el numero por 10 se obtiene:')
valor_int= int(valor)#Esta funcion convierte la cadena de caracteres en enteros
print(valor_int * 10)

nombre = 'david'
apellido = 'cervantes'
nota = 'Eres un ganador del oro'

nombre_CAP = nombre.capitalize()#Coloca el primer caracter en mayusculas
apellido_CAP = apellido.capitalize()
un = nota.find('un')#Encuentra en que posicion empieza este valor
texto = nota[8:]#Muestra los caracteres comprendidos entre estos valores

print(nombre_CAP + ' ' + apellido_CAP)
print(un)
print(texto)

#Expresiones
import re

codigo_5_digitos = '12345'
codigo_9_digitos = '12345-6789'
Telefono = '123-456-7890'

regex_5_digitos = r'\d{5}'#Aqui le pedimos que buscara grupos de 5

print(re.search(regex_5_digitos,codigo_5_digitos))#Con la funcion re hara la busqueda , le damos dos valores, cuanos buscara y en donde
print(re.search(regex_5_digitos,codigo_9_digitos))
print(re.search(regex_5_digitos,Telefono))

# ARCHIVOS
archivoN = open('valores.txt', 'rt')#Abre este archivo y con rt le decimos que solo sera de read(Lectura)
archivoS = open('valores_totales.txt', 'wt')#hace lo mismo pero con wt indicamos que solo sera escritura, pero si no existe el archivo lo creara
print('Procesando Entrada')
suma = 0;
for linea in archivoN:
    suma += int(linea)
    print(linea.rstrip(), file=archivoS)#Esta linea hace que cada linea que se lee en ArchivoN se vaya a ArchivoS
print('\nTotal: ' + str(suma), file=archivoS)#Imprime un espacio y le concatena un string, y se imprime en el archivo
archivoS.close()
print('Salida completa')