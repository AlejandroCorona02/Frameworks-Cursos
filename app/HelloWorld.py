from flask import Flask #Aqui se importan las librerias

app = Flask(__name__) #Aqui se crea una instancia que sea igual a la variable app, esto representa la app de flask
#Con el de arriba indicamos que este archivo sera nuestra aplicacion, y todos los recursos los buscara en este programa, por asi
#decirle le indicamos que este es nuestro main, por ende aqui deberia de estar cualquier cosa usada en el programa 

@app.route('/') #Aqui se crea una ruta,lo que hay entre parentesis indica que esta es la ruta principal y debe estar asociado a una funcion que sera un lista
def hello():
    return 'Hola Mundo'