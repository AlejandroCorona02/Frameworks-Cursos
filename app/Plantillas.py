from flask import Flask, render_template#Con render template lo que pasa es que podemos "Mandar llamar" un 
#html desde la carpeta templates, nombre que debe tener todo el tiempo pues es lo que busca
app = Flask(__name__)

#FILTROS PERSONALIZADOS
#Mas que nada es para que puedas hacer filtros como tu quieras, en este ejemplo lo 
#que se usa es una fecha pero muy larga, por ende se crea un filtro para mostrarla como nostroso deseemos

@app.add_template_filter #Con este puede ser registrado el filtro, claro antes de la funcion
def today (Date):# Esta es nuestra funcion con nombfre today
    return Date.strftime('%d-%m-%Y')#Aqui indicamos que queremos recibir, por eso se coloca la d, m y Y,
#Esto es nuestro dia mes y año

#app.add_template_filter(today,'today') # Esta es otra manera como podemos agregar el filtro, solo que aqui este esta 
#debajo de la funcion, pues necesita que este creada desde el comienzo
from datetime import datetime #Con esto importamos la fecha

#FUNCIONES PERSONALIZADAS
#Realmente las funciones pueden ser usadas de distintas formas y con flask podemos hacerlas tan sencillas como
#llamrlas y es todo, sin necesidad de indicarle al programa que es una variable y que la lea y cosas por el estilo
#como de la siguiente manera
@app.add_template_global#Con esta linea de codigo se registra la funcion en todo los programas y ya no es necesario
#indicar la variable ahora solo se utiliza y ya
def repeat (s,n):
    return s*n

@app.route('/')
@app.route('/Index')
def Index():
    name = 'David' #Aqui creamos una variable, para poder hacer uso de esta en el archivo html
    Friends = ['Alan','Jaime','Diego','Luis','Juan','Monse','Camis']
    Date = datetime.now()#Con esta linea importamos la fecha actual esto gracias a la libreria
    
    return render_template('index.html', 
                           name = name, 
                           Friends = Friends,
                             Date = Date)#aqui solo hacemos uso de la biblioteca con render_template, pero el 
#nombre que hay entre parentesis es el html que queremos mostrar y eso seria todo, aclarando que este html 
#debe estar dentro de la carpeta templates, despues de la coma ponemos el nombre de la variable asigandosela
#asi misma ya que no podemos colocarla de forma directa

