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
@app.route('/Index')
def Index():
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
    Pruebas = 'Si'
    return render_template('Prueba_1.html', 
                           Pruebas = Pruebas)

@app.route('/')
def General():
    print(url_for('Prueba',Pruebas = 'Si'))
    print(url_for('Index'))
    