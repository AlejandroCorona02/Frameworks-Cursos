#A continuacion el codigo mostrado se enfoca en los formularios
#por ende a parte de los formularios nada se comentara, si lo
#que quieres saber es que pasa con las primera lineas de codigo 
#se encuentran en el archivo Rutas.py


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



@app.route('/Contenido')
@app.route('/Contenido/<Name>')
@app.route('/Contenido/<Name>/<int:Age>')
@app.route('/Contenido/<Name>/<int:Age>/<email>')
def Contenido(Name = 'Alex' , Age = 21, email = 'Alvyajalo@ajskjsa'):
    My_data = { 
        'Name' : Name, 
        'Age'  : Age,
        'email': email
    }
    return render_template('Variables.html', data = My_data)

from markupsafe import escape
@app.route('/code/<path:code>')
def code(code):
    return render_template('Prueba_2.html')

@app.route('/auth/Registro')
def Registro():
    return render_template('auth/Registro.html')