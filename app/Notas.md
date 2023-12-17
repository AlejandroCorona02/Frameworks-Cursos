LINK DEL CURSO: https://www.youtube.com/watch?v=W-SfC_V7P6o
Estudiar y practicar con FrameWorks Web, Los mejores son Flask para proncipiantes y Django para los mas experimentados, aunque deberia empezar con cursos de flask para despues saltar a django

## FRAMEWORKS 
Realemtne son como programas que ya nos dan muchas cosas relacionadas con la web, como cuestionarios, inicios de sesion y cosas que podrias hacer con html pero todo esto con distintos lenguajes como seria python, para esto los frameworks nos dan una serie de instrucciones con las que podemos trabjar y son como librerias que se mandan llamar para lograr eso


## FLASK
Microframework de python para para desarrollar aplicaciones web, nos da chance hacer aplicaciones rapido y con poco codigo, proporcionada enrutador url y manejar solicitudes http y respuestas
Nos da la oportunidad de elegir las librerias que queremos, es muy flexible en cuestion a herramientas, paquetes y tecnologias, podemos personalizar flask en nuestras aplicaciones, gran comunidad y documentacion
Bajo nivel de abstraccion lo que permite control sobre la aplicacion. Flask es facil de integrar con otros servicios

## PARA COMENZAR
Lo primero que hacemos es crear un entorno virtual y para esto solo nos dirigimos a la carpeta deseada desde el cmd, y creamos un directorio ( **Mkdir**  ) ya aqui se crea el entorno virtual con **"python -m venv EntornoVirtual"**, siendo que "EntornoVirtual" Puedes ser cambiado por el nombre que quieras ya que este sera el nombre del entorno virtual, todo esto trabajado desde python, pero puede cambiar, una vez creado ahora tiene que ser activado para esto desde cmd y con el comando "cd" debemos dirigirnos a "EntornoVirtual",En este caso por que asi se llama mi entorno virtual, despues a la carpeta Scripts, y ahora **sin usar cd**, Activate, cuando se ejecute este comando se tomara su tiempo y despues a un lado de la direccion en la cmd, entre parentesis nos arrojara el nombre de nuestro Entorno virtual, aqui es donde se trabajara pues es algo asi como si estuvieramos fuera de nuestra misma PC, asi todo lo que se vaya a trabajar en este proyecto se quedara en este proyecto, para desactivar el entorno virtual se usa el comando **"deactivate"**, una vez que el entorno este activo, desde la carpeta de la aplicacion fuera de la carpeta del entorno virtual abrimos Visual studio, mediante **"code ."**, aqui ya podemos comenzar con el programa, lo estas haciendo en este direccion "C:\Users\ASUS\Documents\Python_Autodidacta\Frameworks\app", el programa se comentara, una vez echo el programa solo se coloca un texto en este para que se muestre, pero este tiene su chiste para correrlo ya que debe de ser desde la terminar y usando el siguiente comando **"flask --app HelloWorld run"**, Siendo que HelloWorld es el nombre del programa puede cambiar, y cuando se haga esto creara un servidor local para mostrarte esa informacion, el cual se puede acceder con la url que te arroja. 

## CONTINUANDO

Modo depurador es para que los cambios se vean de manera real en el servidor asi cada error que se tenga este sera mostrado en el cmd y por ende el servidor no se levantara o se caera, es buena practica ya que se puede hacer mas eficaz la busqueda de erorres, para activar el modo debug debemos correr el programa pero con el siguiente comando **"flask --app hello --debug run"**, con este modo activado no necesitamos correr el servidor cada que haya un cambio asi solamente se recarga la pagina y es todo.

En las url se puede enviar informacion de todo tipo no necesariamente tiene que ser solo texto podemos hacer uso de los datos de html que nos arroja la misma pagina logrando mandar datos tales como un pie de pagina, un titulo o cualquier cosa siempre y cuando sea datos de html, tambien podemos tener varias rutas que manden llamar o usean la misma definicion asi usando el mismo texto para distintas url


## VARIABLES

Este tema quizas sea mejor explicado en el programa como tal pero es escencial que se explique aun aqui, la idea principal es que el usuario pueda darnos datos de cualqueir tipo esto para que podamos trabajar con ellos ya sea para solo regresarlos o para que estos puedan ser necesarios para datos de comparacion o cosas como esas, para esto los datos de primeras los daremos mediante la url, se coloca el nombre de la variable dentro de la url y solo se especifica en la definicion que sera usada, despues solo la usaremos poiendola entre corchetes en el texto que regresemos pero es necesario que cambiemos algo en comparacion con los programas anteriores ya que debemos de colofar una f despues del returno esto para que se resete los datos y pueda mostrarlos, ademas de que si no se coloca la variable no la tomara en cuenta y solo las colocara como tal, ahora si lo que queremos es que nos arroje 
distintos resultados para cada uno de los url solo anidamos los url y colocamos if para saber si estas si se estan usando y si no se usan que mande algo dependiendo a lo que se use.

Un error que puede suceder que seria no mantener segruo nuestro sitio/aplicacion ya que aqui se puede hacer uso de comando html para hacer cosas no deseadas en la aplicacion, como alertas y cosas del estilo, por ejemplo con el codigo comentado a continuacion, podriamos recibir una variable como  <script>alert("CHUPALA")</script>, haciendo que salten alertas no esperadas, asi arruinando el programa. Para evitar lo anterior se puede hacer uso de los escapes de html que es mas que una buena practica lo mas necesario para evitar cosas no deseadas, para esto importamos escape desde markupsafe, esto ya viene instalado cuando instalamos Flask, asi pues importada en el codigo la ponemos antes de returnar la funcion

## Plantillas con jinja2 y html
Es un motor de plantillas para python para generar contenido html, xml y datos en tiempo de ejecucion, esta libreria ya se encuentra una vez que instales flask, con esto podemos hacer herencia de plantillas

## HTML
A partir de aqui el curso toma otra ruta que mas que nada lo que hace explicar parte de html y como esta puede ser utilizada para crear nuestra pagina, nos habla de como con las librerias podemos llegar a hacer uso de archivos html como tal pero no solo se queda ahi ya que esta libreria tambien hace uso de los llamados bloques lo cuales mas que nada sirven para no tener que repetir cierta informacion o sustituir cosas que parezcan redundantes, tambien nos explica como podemos hacer uso de las estructuras de datos, como lo son el if, for, etc.

Para editar lo que se va a mostrar en la pantalla existen los filtros estas pueden ser utiles para modificar la informacion segun lo que vayamos a necesitar