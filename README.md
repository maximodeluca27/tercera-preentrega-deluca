tercera preentrega del curso de python de coderhouse 
Dentro del proyecto hay una aplicacion llamada avion donde se incluyen los modelos a utilizar

# comandos

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