#A continuacion el codigo mostrado se enfoca en los formularios
#por ende a parte de los formularios nada se comentara, si lo
#que quieres saber es que pasa con las primera lineas de codigo 
#se encuentran en el archivo Rutas.py


from flask import Flask, render_template, url_for, request
app = Flask(__name__)
app.config.from_mapping( SECRET_KEY = 'dev') # Cuando nosotros 
#trabajamos en cosas como formualrios o registro de usuarios 
#es buena practica hacer uso de esta secret key, aunque algunos
#proyectos la necesitaran de manera obligada

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
        if len(username) >= 8 and len (username) <= 15 and len(password) >= 6 and len(password) <= 15:
            return f"Hola {username}, tu contraseña es {password}"
        else:
            error = "El usuario es invalido ya que debe de ser de entre 8 y 15 caracteres asi como la contraseña que debe ser de entre 6 y 15 caracteres"
           
            return render_template('auth/Registro2.html',error = error)
    
    return render_template('auth/Registro2.html')


#A partir de aqui se comienza con la parte de formulario
#mediante bibliotecas
#WTFORM

from flask_wtf import FlaskForm#Importamods los modulos que
#crean los formularios 

from wtforms import StringField, PasswordField, SubmitField
#En este campo lo que hacemos es importar los distintos inputs
#que dependen a lo que necesitamos aqui por ejemplo importamos
#3 el string para palabras (username), el password para que 
#sea secreta la contraseña y submit que funciona principalmente
#para enviar los datos es como quien dice el boton de enviar
#los datos

from wtforms.validators import DataRequired, Length #Aqui 
#estamos importando estos datos pues son validadores y lo 
#que queremos es que el dato sea obligatorio para eso es 
#datarequired y para el maximo y minimo de caracteres 
#usamos length

class RegisterForm(FlaskForm): #Aqui como tal se crea el 
#formulario por ende se crea una clase y hereda flaskform
#que es para crear los formualrios como tal
    

    username = StringField("Nombre de usuario: ",validators=[DataRequired(),Length(min = 6, max = 10)])
#Aqui dependiendo de lo que queramos solo sera esta linea de 
#codigo y entre comillas se pondra lo que dira la label
#del cuadro de texto, en este caso esperamos solo una 
#string por eso el uso de stringfield, en los siguientes
#Casos se necesita password y submit por ende esos se usan
    password = PasswordField("Contraseña:  ",validators=[DataRequired(),Length(min = 6, max = 10)])
#Tambien tanto en username como password tenemos una variable
#llamda validators estos son los que se importaron con 
#anterioridad, mas que anda lo que hacemos es hacer el campo 
#obligatorio con DataRequired y pedimos un maximo y minimo de 
#caracteres con length
    submit = SubmitField("Registrar ")



@app.route('/auth/WTForm', methods = ['GET', 'POST'])
def WTF():
#Para dibujar nuestro formulario lo primero que haremos ser a
#crear una instancia en la que mandemos llamar Register form
    form = RegisterForm()
    if form.validate_on_submit(): #Esta condicion esta basado
#en si los datos se enviaron y se hizo lo del metodo post, pero
#este metodo tambien es necesario validarlo en el html que se
#este trabajando
        username = form.username.data#una vez que valida que
#los datos ya estan enviados ahora a la variable le da el valor 
#que se encuentre en el campo de textro de user name pero solo
#los datos por eso el ".data"
        password = form.password.data
        return f"Hola {username}, tu contraseña es {password}"



    return render_template('auth/WTForm.html', form = form)#Se 
#manda la instancia al archivo html para que este lo detecte 
#una variable y podamos usar