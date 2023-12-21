from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.add_template_global
def repeat (s,n):
    return s*n

@app.add_template_filter 
def today (Date):
    return Date.strftime('%d-%m-%Y')

from datetime import datetime

@app.route('/')
def Index():
    #A continuacion se colocan los print para las url para hacer que el programa 
    #los cree y no tengamos la necesidad de cambiar todo de manera manual, asi
    #Solo escribimos lo siguiente y sera todo
    print(url_for('Index'))
    print(url_for('Prueba', Prueba = 'Si'))
    print(url_for('Contenido',data = 'My_data'))
    print(url_for('code', code = 'print("Hola")'))
    
    
    name = 'David' 
    Friends = ['Alan','Jaime','Diego','Luis','Juan','Monse','Camis']
    Date = datetime.now()
    
    return render_template('index.html', 
                           name = name, 
                           Friends = Friends,
                             Date = Date)

@app.route('/')
@app.route('/Prueba')
def Prueba():
    Prueba = 'Si'
    return render_template('Prueba_1.html', 
                           Prueba = Prueba)


#Aqui comenzaremos a ver la parte de variables pero aplicadas a 
#los html y no aqui en python como usualmente los estamos viendo
@app.route('/Contenido')
@app.route('/Contenido/<Name>')
@app.route('/Contenido/<Name>/<int:Age>')
@app.route('/Contenido/<Name>/<int:Age>/<email>')
def Contenido(Name = 'Alex' , Age = '21', email = 'Alvyajalo@ajskjsa'):
    #A esto se le llama estructura de datos
    My_data = { #Este comenta el curso es un diccionario una especie de 
        #almacenamiento de variables que aqui se obtienen y son enviadas
        #a los html que lo requieran
        'Name' : Name, 
        'Age'  : Age,
        'email': email
    }
    return render_template('Variables.html', data = My_data)#Aqui por lo
#que entendi es que es una especie de carpeta donde almacenamos todas
#nuestras variables, para asi solo llamar a la carpeta y no sera 
#necesario hacer toda la declaracion de variables en algun otro lado

from markupsafe import escape
@app.route('/code/<path:code>')
def code(code):
    return render_template('Prueba_2.html')