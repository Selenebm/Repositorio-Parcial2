# **Creación de página web** 
Para este proyecto se hizo la realización de una pagina web haciendo uso de visual studio code, en este ponemos en práctica la creación de una base de datos siendo en este caso los productos que queremos presentar, distribuimos el codigo en diferentes carpetas que nos ayudara en la distribución de este mismo

## **Carpetas:**
+ env: Entorno virtual
+ Static: Recursos visuales de la página
+ Templates: área de trabajo enfoncada en de la estructura visual maneja siendo HTML, en esta tenemos:
  - base: Estructura fudamental de las paginas HTML realizadas
  - index: Distribución de la lista de productos
  - producto: Presentación de cada producto
+ gitginore: Registro de los archivos
+ Crear_db.py: Apartado de la base de datos
+ main.py: Aplicación principal donde se crea la página
+ web2.sqlite3: Base de datos

# **Funcionalidades y aprendizajes:**
+ Consulta de la base de datos: Utiliza el archivo Crear_db.py para cargar los datos de tus productos desde la base de datos web2.sqlite3. Con la categoría, el nombre, el precio, la descripción y la ruta de la imagen asociada a cada producto.
+ Diseño HTML: Crea una estructura HTML en el archivo producto.html para mostrar la información de cada producto. Deberías tener elementos HTML para mostrar la imagen del producto, su categoría, nombre, precio y descripción.
+ Integración de datos con Flask: En el archivo main.py, utiliza Flask para crear una ruta que maneje la visualización de los productos. Carga los datos de los productos desde la base de datos y pasa estos datos a la plantilla producto.html para renderizarlos en la página.

# **¿Porque es util este proyecto?**
La creación de una página web utilizando Visual Studio Code es fundamental para establecer una presencia en línea efectiva. Al gestionar productos a través de una base de datos, organizando el código en carpetas específicas y utilizando recursos visuales y estructuras bien definidas, se demuestra un enfoque profesional y organizado. Además, la inclusión de archivos como "gitignore" es práctica de control de versiones, facilitando la colaboración y el seguimiento de cambios. Esto permite ofrecer una experiencia interactiva a los usuarios, lo que es crucial para el éxito del proyecto al proporcionar acceso global y mejorar la percepción del mismo.

# **Cómo pueden comenzar los usuarios con el proyecto.**
Para que los usuarios puedan comenzar con el proyecto, primero necesitarán instalar Visual Studio Code y configurar un entorno virtual. Luego, pueden clonar el repositorio desde un sistema de control de versiones, como Git, y seguir las instrucciones proporcionadas en este link: https://www.youtube.com/watch?v=VzjxGv6t_G0

## **Autores del proyecto.**
+ Selene Belalcazar Muñoz.
### **Referencias**
+ Diego F Marin Lozano - https://www.youtube.com/watch?v=VzjxGv6t_G0


