# Nombre del Proyecto 
> VirtualPLanes


# Breve Explicacion
> Cree un proyecto django para fanaticos de aviacion comercial. Registra aviones, y puede borrar, crear y modificar aeropuertos internacionales. 

# Explicacion Tecnica
esta el proyecto que tiene el nombre de la preentrega, y dentro de el cree las aplicaciones avion y core. Hay dos clases, aeropuerto y avion, registradas ambas en el models.py de la app avion. Tambien registre la clase usuario a la cual se puede vincular los usuarios logueados con nombres y telefonos celulares, ademas de una foto de perfil. Las fotos se pueden ver desde "media/avatares". Desde el archivo urls.py llamo a las distintas vistas en el archivo views.py. El core es la aplicacion principal y avion la secundaria. Tambien implemente formularios en el archivo forms.py, que desde las vistas podemos llamarlo para utilizarlo en la creacion de aviones, o en el CRUD de aeropuertos. 

# Acerca de Mi 
Cree una seccion acerca de mi, a la cual se puede acceder pulsando contacto

# Comandos
`mkdir TERCERA-PREENTREGA-DELUCA`
> Crea una carpeta llamada project

`ls`
> Muestra la lista de archivos

`cd TERCERA-PREENTREGA-DELUCA`
> Cambia de carpeta

`pwd`
> Muestra la ruta actual

`python -m venv .venv`
> Crea un entorno virtual llamado .venv

`source .venv/bin/activate`
> Activa el entorno virtual en Linux o Mac

`.\venv\Scripts\activate`
> Activa el entorno virtual en Windows

`pip list`
> Muestra la lista de paquetes disponibles en el entorno virtual

`pip install django`
> Instala Django

`mkdir project`
> Crea el directorio del proyecto de Django

`cd project`
> Nos introducimos en el directorio

`django-admin startproject config .`
> Crea un proyecto en el directorio actual

`python manage.py runserver`
> Ejecuta el servidor

`http://127.0.0.1:8000/`
> Ejecutar en el navegador

`python manage.py startapp avion`
> Crea una app

`python manage.py makemigrations`
> Crea archivos Python para preparar la migración

`python manage.py migrate`
> Ejecuta las migraciones (SQL) para crear o modificar la base de datos

`python manage.py createsuperuser´ admin 
> Crea una usuario administrador para acceder a la app admin

## Crear archivo de requisitos: requirements.txt

`pip freeze >> requirements.txt`

`pip install -r requirements.txt`