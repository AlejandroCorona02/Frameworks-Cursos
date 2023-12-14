from flask import Flask #Aqui se importan las librerias

app = Flask(__name__) #Aqui se crea una instancia que sea igual a la variable app, esto representa la app de flask
#Con el de arriba indicamos que este archivo sera nuestra aplicacion, y todos los recursos los buscara en este programa, por asi
#decirle le indicamos que este es nuestro main, por ende aqui deberia de estar cualquier cosa usada en el programa 

@app.route('/hello') #Aqui se crea una ruta,lo que hay entre parentesis indica que esta es la ruta principal, nos arrojara un url que tendra
#numeros hasta antes del slash(/), despues lo que escribamos sera lo que debemos poner para ver la funcion asociada y debe estar asociado a 
#una funcion, asi cada que se solicite el link arroje algo de regreso en este caso solo sera un texto 

def hello():
    return 'Hola Mundo'

@app.route('/Inicio')#Podemos usar distintas rutas pero tenemos que tener cuidado en que las url no sean las mismas
def Inicio():#Asi como las definicion no pueden repetirse
    return '<h1>Home Screen</h1>'#No solo podemos enviar texto plano podemos hacer que sean datos de html, como aqui

@app.route('/')#Con esto lo que hacemos es que ya sea la url principal o con la palabra index siempre veremos lo mismo
@app.route('/Index')
def Index():
    return '<h1>Index</h1>'


#A continuacion la variable que se usara y se mostrara es mediante URL, ahi colocaremos la variable que queramos
@app.route('/Nombre/<name>')#Cuando usamos los signos de mayor que y menor que entre una palabra asi indicamos que es una
#variable con el nombre con el que se indica
def Name(name):#Para hacer uso de esta variable le tenemos que decir a la funcion que esta sera utilizada, con colocando
    #el nombre de la variable dentro del parentesis
    return f'<h1>Hola {name} </h1>'#Aqui es escencial que en el return usemos la f que indica que se hara un reseteo 
#Y para usar la variable se coloca entre un par de corchetes


#Si queremos especificar que se use un tipo de variable en especifico (String,int, float, path, uuid), se coloca antes
#de la variable como se muestra a continuacion
@app.route('/Edad/<int:Edad>')
def Edades(Edad):
    return f'<h1>Tu edad es {Edad} </h1>'

#Aunque claro si lo queremos podemos colocar muchas variables en la misma url incluso especificandolas o no
@app.route('/Datos/<Nombre>/<int:Age>')
def Datos(Nombre, Age):
    return f'<h1>Hola {Nombre}, Tu edad es {Age}? </h1>'


#Ahora si lo que queremos es dependiendo al url, arrojar un dato podemos hacer lo siguiente, se les dara
#nombre a las url para mencionarlas mas adelante y estas tengan mas sentido
@app.route('/Datos1')#URL SOLA
@app.route('/Datos1/<Name1>')#URL NOMBRE
@app.route('/Datos1/<Name1>/<int:Age1>')#URL COMPLETA
def Datos1(Name1 = None , Age1 = None):#Aqui definimos las variables en 0, lo que quiere decir que si no les damos 
#valor tendran un valor nulo y en base a esto podemos comenzar a trabajar

    if Name1 == None and Age1 == None:#En este caso es como si nos fueramos a la url Sola, ya que en esta no
#cambiamos el valor de las varables por ende siempre son none
        return '<h1>Hola mundo :)</h1>'
    
    elif Age1 == None:#Aqui es como si estuvieramos en la url Nombre, esto por que al cambiar el nombre age 
#es la unica variable que aun tiene le mismo valor
        return f'<h1>Hola {Name1} :)</h1>'

    else:#Esta es la URL completa ya que aqui los das valores se les asigno valor mediante la url y asi ninguno vale none
        return f'<h1>Hola {Name1}, Tu edad al doble es {Age1 * 2} </h1>'
