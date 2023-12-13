from flask import Flask #Aqui se importan las librerias

app = Flask(__name__) #Aqui se crea una instancia que sea igual a la variable app, esto representa la app de flask
#Con el de arriba indicamos que este archivo sera nuestra aplicacion, y todos los recursos los buscara en este programa, por asi
#decirle le indicamos que este es nuestro main, por ende aqui deberia de estar cualquier cosa usada en el programa 

@app.route('/hello') #Aqui se crea una ruta,lo que hay entre parentesis indica que esta es la ruta principal, nos arrojara un url que tendra
#numeros hasta antes del slash(/), despues lo que escribamos sera lo que debemos poner para ver la funcion asociada y debe estar asociado a 
#una funcion, asi cada que se solicite el link arroje algo de regreso en este caso solo sera un texto 

def hello():
    return 'Hola Mundo'