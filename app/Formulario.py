#A continuacion el codigo mostrado se enfoca en los formularios
#por ende a parte de los formularios nada se comentara, si lo
#que quieres saber es que pasa con las primera lineas de codigo 
#se encuentran en el archivo Rutas.py


from flask import Flask, render_template, url_for, request
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

@app.route('/auth/Registro', methods = ['GET', 'POST'])#por lo
#que se hasta ahora post y get son para indicar que se reciben
#y se envian  datos
def Registro():
    if request.method == 'POST':#Enviamos datos por ende se
#usa el condicional para pregunar si los esta recibiendo, si
#los recibe entonces pasara a hacer lo siguiente que en este 
#solo sera imprimir las variables que son enviados
        username = request.form['username']
        password = request.form['password']
        return f"Hola {username}, tu contraseña es {password}"
    return render_template('auth/Registro.html')


@app.route('/auth/Registro2', methods = ['GET', 'POST'])
def Registro2():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return f"Hola {username}, tu contraseña es {password}"
    return render_template('auth/Registro2.html')