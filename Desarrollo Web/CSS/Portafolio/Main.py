from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/')
@app.route('/Home')
def Home():
    return render_template('Home.html')

@app.route('/')
@app.route('/AboutMe')
def AboutMe():
    return render_template('AboutMe.html')

#En si esta parte sera mas para hacer distintos html 
#para cada uno de los proyectos y darles pagina a cada uno de ellos
#@app.route('/')
#@app.route('/Proyectos')
#def Proyectos():
#    return render_template('Proyectos.html')

