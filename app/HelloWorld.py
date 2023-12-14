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
