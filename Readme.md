<center><h1>API Python implementando Flask</h1></center>

Este proyecto es un prototipo para ser aplicado como API Rest. Utiliza tecnologias como Flask, git(github en este caso), docker y archivos Json. Este trabajo es ideal para un API muy simple y ligero. Aconparado de Django por ejmplo que es de más alto nivel y con más funcionalidades integradas.

Espero que te sea de provecho este trabajo, y porque no, te aporte en futuros trabajos. 

## Ruta base configurada en este repositorio
1. https://localhost:5000/api/v1/

### MySQL

1. Descargar [MySQL](https://www.mysql.com/downloads/)
2. Instalar
   > **_Nota:_** La instalación de MySQL, es opcional. En su lugar puede usar la base de datos al entorno correspondiente, solicite el mismo a quién corresponda.

### Entorno

1. La arquitectura de esta API es en Flask

### Proyecto

1. Clonar el repositorio
2. Dentro de la carpeta del proyecto encontrarás un archivo `.env.example`, duplícalo y renómbralo como `.env`
3. Cambie las variables de entorno en el archivo `.env` para que se ajusten a su entorno

## Comandos necesarios para iniciar esta API

### Archivos env

1. sudo apt install python3-venv

### Entorno virtual

2. python3 -m venv venv

### Dependencia de mysql
3. pip install Flask Flask-SQLAlchemy pymysql python-dotenv marshmallow

### Instalar
4. sudo apt install pipx

### Paquetes
5. pipx install flask
6. pipx install flask-sqlalchemy
7. pipx install pymysql
8. pipx install python-dotenv
9. pipx install marshmallow

### Docker build
10. docker-compose up --build

### mysqlclient linux
11. sudo apt update
12. sudo apt install pkg-config libmysqlclient-dev
13. pip install mysqlclient


## Levantar el servicio
1. source venv/bin/activate
2. python run.py

## Para abandonar el servicio de la API
1. crtl + c
2. deactivate 
