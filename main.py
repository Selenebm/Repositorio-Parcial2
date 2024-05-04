from flask import Flask, render_template
import sqlite3
from pprint import pprint

#Carga de los datos
conexion = sqlite3.connect('web2.sqlite3')
conexion.row_factory = sqlite3.Row # Modo diccionaria 
cursor = conexion.cursor()
cursor.execute("""SELECT * FROM productos; """)
productos = [ dict(producto) for producto in cursor.fetchall()]
cursor.close()
conexion.close()

#Aplicación
app = Flask(__name__)

#Rutas
@app.route('/')
def ruta_raiz():
    return render_template('index.html', productos=productos)
#Programa principal
if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)
    