#Importar la libreria para gestionar la DB
import sqlite3

#Establecer la conexion
conexion = sqlite3.connect('web2.sqlite3')
cursor = conexion.cursor()

#Eliminar la tabla en caso de que exista
cursor.execute("""DROP TABLE IF EXISTS productos; """)

#Crear la tabla 
cursor.execute("""CREATE TABLE IF NOT EXISTS productos (
               id INTEGER PRIMARY KEY, 
               categoria TEXT NOT NULL, 
               marcar TEXT NOT NULL, 
               nombre TEXT NOT NULL, 
               descripcion TEXT NOT NULL, 
               precio INTEGER NOT NULL
               ); 
               """)

#Insertar primeros datos
datos = [
    (104, "Juguetes", "Sanrio", "Hello Kitty Peluche", "Peluche suave de Hello Kitty, ideal para abrazar.", 20000),
    (267, "Ropa", "San-X", "Camiseta Rilakkuma", "Camiseta de algodón con estampado de Rilakkuma, perfecta para el verano.", 145000),
    (393, "Accesorios", "Q-Lia", "Bolso Kawaii de Frutas", "Bolso de hombro con diseño de frutas kawaii, con cierre de cremallera.", 76250),
    (467, "Hogar", "Amuse", "Taza Alpacasso", "Taza de cerámica con diseño de Alpacasso, apta para microondas y lavavajillas.", 88000),
    (581, "Papelería", "Crux", "Cuaderno Sumikko Gurashi", "Cuaderno de espiral con diseño de Sumikko Gurashi, 80 hojas.", 120000),
    (678, "Electrónica", "Tokidoki", "Auriculares Donutella", "Auriculares inalámbricos con diseño de Donutella, con estuche de carga.", 330000),
    (799, "Juguetes", "Tasty Peach Studios", "Peluche Meowchi", "Peluche suave de Meowchi, con relleno de felpa de alta calidad.", 67000),
    (817, "Ropa", "Cinnamoroll", "Vestido Cinnamoroll", "Vestido de algodón con estampado de Cinnamoroll, perfecto para ocasiones especiales.", 152000)
]

cursor.executemany("""INSERT INTO productos VALUES (?, ?, ?, ?, ?, ?);""", datos)

#Grabar
conexion.commit()
conexion.close()