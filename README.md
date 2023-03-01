# Ejercicio de Python + FastApi + MariaDB y Ubuntu 22.04
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Introduccón
Para el ejericio se trabajo con Visual Code y se instalo  Python + FastApi + BD Maria.  Sencillo ejemplo para compreder como crear API y conocer todo el pontencial de FAST-API
- Desarrollo con Visual Code + Python
- Conexion conexion a BD MariaDB
- Uso de FastApi con Python
- Levantar el servidor web unicorv

Ademas se trabajo con Docker y se creo un contenedor de MariaDB


## Instarla/Activar paquetes en Linux
Al momento de escribir esto, se usa Ubuntu 22.04
1. Anaconda, activar entorno virtual fast-api
```sh
conda activate fast-api
```
2. Docker:  Activar el contenedor de MariaDB (mysql)
```sh
sudo docker ps -a
sudo docker start mysql
```
3. Servidor uvicorn para Fastapi
```sh
uvicorn app:app --reload
```
4. Actualizar conda y su entorno virtual fast-api
```sh
conda update --all -n fast-api
```
5. Instalar sqlalchemy
```sh
conda install -c conda-forge sqlalchemy --name fast-api
```
6. Instalar pydantic
```sh
conda install pydantic  -n fast-api
```
7. Instalar cryptography
```sh
conda install -c anaconda cryptography --name fast-api
```
8. Instalar pymysql
```sh
conda install -c anaconda pymysql -n fast-api
```


> La guia incluye links para instalar lo necesario
> por ejemplo: Python, Anaconda, etc.

## Links de Intalación
Para el ejercicio se usaron estos enlances para instalar el ambiente.  Se trabajo con Ubuntu 22.04
| Plugin | Install |
| ------ | ------ |
| Python | https://www.python.org/downloads/ |
| Anaconda | https://www.anaconda.com/products/distribution |
| Fast API | https://fastapi.tiangolo.com/#installation |
| Uvicorn | https://www.uvicorn.org/ |
| Docker  | https://docs.docker.com/engine/install/ubuntu/ |
| MariaDB con Docker | https://mariadb.com/kb/en/installing-and-using-mariadb-via-docker/ |

