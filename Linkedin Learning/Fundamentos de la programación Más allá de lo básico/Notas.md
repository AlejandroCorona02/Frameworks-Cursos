## CONOCIMIENTOS PREVIOS
Variables, Funciones, Logica condicional

## Pylint-Extension de vscode

## Colecciones = variables
Son varias variables que sdean similares
asi no hay muchas variables solo datos 
relacionados, los datos pueden almacenmarse
bajo la misma variable, sintaxis simplificada
Para trabajar con estas colecciones es tan 
sencillo como solo indicarle el numero de elemento
en python podemos hacer listas de variables de 
distinto tipo, ya sdean cadenas, numeros o 
valores booleanos

## Tipos de coleccion: 
-Lista:
    ciudades = [
    'Mexico',
    'Aguas',
    'Micho',
    'Colima'
    ]

## Diccionarios
Son etiquetas que podemos colocarle a las 
colecciones, en si son listas pero en vez 
de tener numero asignado para cada valor 
tenemos un nombre que nosotros le podemos 
otorgar

## Colecciones mutables e inmutables
Son aquellas listas que nos permiten cambiar 
lo valores de estas, siendo que sean llamdas mutables
tambien existen listas que una vez creadas es imposible 
cambiar valores de sus listas a estas se les llama
inmutables

## ITERACIONES
Repetir procedimiento hasta que se alcanza el fin
se necesitan especificar los datos, se describe que 
pasa con los datos en cada iteracion, y se idnica cuando 
se detiene el ciclo
**For**
Se usa mucho paa hacer determinada tarea que requiera de 
instrucciones repetitivads pero con distintos elementos
de una lista, asi podremos usar cada uno de los valores
para algo distinto

## CODIGOS COMPARTIDOS
Se pueden encontrar de distintos tipos, el primero que se 
revisa es el modulo que es en si una variable o una funcion
esto se logra a traves de lo que se conoce como importacion,
tambien es comun usar distitnas funciones que vienen contempladas
en un mismo modulo, a esto se le llama paqueteria o libreria,
cuando el conjunto de codigo no se utiliza a la vez, si no de 
manera especifica se le llama Framework

**Acontinuacion**
Como crear nuestros propios modulos, esto es tan sencillo
como abrir otra hoja de archivo para que aqui este la funcion 
a crear como modulo y despues se importa solo con el nombre 
del archivo y para utilizar la funcion se coloca el nombre y
se le pone un punto seguido del nombre de la funcion que deseamos
utilizar del archivo importado y se coloca unos parentesis despues
donde iran las variables que indique la funcion

## LIBRERIAS Y FRAMEWORKS 
Son colecciones de herramientas de software, una libreria nos da
herramientas para construir una aplicacion, el framework tiene
muchas decisiones ya tomadas, por lo que si al hacer un proyecto no 
tenemos un enfoque especifico es mucho mejor usar librerias en cambio
si tenemos un enfoque y existe un framework que se ajuste a nuestro
proyecto es mucho mejor usar frameworks

**Ejemplos de librerias** 
TensorFlow y Pandas, estos se usan para el aprendizaje automatico,
NumPy y SciPy, se usan para operaciones matematicas

**Ejemplos de Frameworks**
Django y Flask, son usados para la gestion de contenido Web

## Strings
**Concatenacion** en si son varias cadenas combinadas en una 
unica cadena para esto se usa el signo de **"+"**, y si queremos
multiplicarlo, sumarlo o lo que sea matematicos con este valor 
necesitamos converetir el valor strin en un valor entero esto se
hace con lo siguiente **valor_int= int(valor)**, solamente a una 
variable se le asigna lo que este en int

Las cadenas se pueden manipular de uno en uno en el ejemplo tomamos
el nombre de una variable y con la funcion **.capitalize** lo que 
hace es tomar el primer valor de la cadena y la convierte en mayuscula

Aunque tambien existe otra funcion como **.find** que funciona para 
saber en que posicion se encuentra cierta palabra

Tambien existe la posibilidad de tomar caracteres de toda la palabra
solamente poniendo el nombre de la variable y entre corchetes un numero
seguido de dos puntos y despues otro numero algo asi **var[2:2]** esto 
solo seria para indicar de donde empieza y donde acaba 

## Expresiones regulares
Con estas mas que nada es para ecnontrar patrones en un texto similar
a si quiseramos encontrar un grupo de tantos numeros de un numero de telefono
como es usado en el ejemplo

## Guias de estilo
Se refiere a como se debe escribir el codigo y en este caso para python
la mas famosa es **PEP-8**, mas que nada es una compilacion de todas las
buenas practicas que se deberian de seguir asi como de conceptos basicos 
del lenguaje, aunque es la mas comun no es la unica guia que existe ya que
esta **La guia de estilo de python de google**, son ayuda para entender 
codigo ajeno

## PSEUCODIGO
Descripcion de lo que intentas hacer en tu codigo, ayuda a realizar la 
estructura del codigo y es para guiarse acerca de lo que se quiere conseguir

## Archivos
Los archivos se pueden abrir desde python y segun lo que se le indique estos 
pueden ser leidos uno a uno o pueden ser sumados todos 

## DEBUGGIN
Depuracion: identificacion y arreglo de fallos
**Hay 3 tipos de errores muy comunes:**
**Error de sintaxis:** El codigo no coincide con las reglas del lenguaje
**Error en tiempo de ejecucion:** Es cuando tiene buena sintaxis pero 
quizas una variable aun no tiene valor asignado
**Error de logica:** Funciona bien pero no es lo que se esperaba, 
el resultado es diferente a lo que queremos
Muchos IDE indican errores a la hora de escribir codigo, algunos como 
VSCode indican con un subrayado de color, a esto se le conoce como **resaltado de sintaxis** , algunos tambien nos ayudan con el **autocompletado**, esto para simplificar 
escribir codigo

**Casos de prueba:** Mas que nada son comandos o scripts diseñados para probar una situacion especifica

## Programacion orientada a objetos
Son paradigmas para estructurar el codigo, la idea de este tipo de programacion es principalmente la idea de partir el programa en otros mas pequeños, estos objetos se comunican y esto hace mas facil de mantener y reutilizar el codigo
En esta programacion cada objeto tiene atributos y comportamientos, **Los atributos** son datos o caracteristicas que tiene el objeto, y cada **comportamiento** es algo que el objeto puede hacer Los atributos se denominan **propiedades** y los comportamientos son **metodos** , ahora bien los metodos se pueden usar para trabajar con sus propiedades del mismo objeto, se crean objetos utilizando un modelo conocido como **clase** una clase describe los atributos y el comportamineto de un objeto

**UTILIZACION DE CLASES**
Es como dar un estandar en la creacion de los objetos para que todos tengan cosas similares, esto nos ayuda a evitar el codigo repetitivo, asi una cantidad de objetos comparten estos objetos y despues solo se personaliza cada uno de los objetos


## MEMORIA
Diferencia entre ram y rom, en los programas lo que no se ocupe necesita ser eliminado de la memoria cache, en algunos lenguajes es posible decidir cuales datos eliminar o no de la ram, a esto se le conoce como **gestion de memoria**, es dificil de implementar y puede causar fugas de memoria, por lo regular en videojuegos es muy implementado debido a su alto consumo de procesamiento, tambien existe **Recolector de basura**
este busca e identifica lo que es posible eliminar de la memoria, pero todo esto en python no es realmente necesario ya que lo tiene incluido por defecto

## MULTIHILOS
Es hacer varias tareas en paralelo, a cada uno de estos se les conoce como hilo y al codigo que se escribe asi se le llama subproceso multiple cada uno de estos necesita bastante memoria de la PC por eso es necesario contemplar el rendimieno de esta, tambien se le llamda **codigo asincrono**