# Lector de JSONPlaceholder
Proyecto en python-django para consumir el API JSONPlaceholder, y guardar la información obtenida en la BD local.

## Instalación
Se descarga el proyecto, y se va a la ubicación del direcotrio principal, se utilizan los siguientes comandos:
```
git clone https://github.com/Jcmantillam/JSONPlaceholder.git
cd jsonplaceholder
pip install -r requirements.txt
python manage.py migrate
```
## Servicios
Se tiene varios servicios requeridos para el CRUD, los recusros soportados son los mismos que aparacen en JSONPlaceholder:
- /posts
- /comments
- /albums
- /photos
- /todos
- /users

### Users
 
 * **URL:** <api/v1/users/>
 
 * **Métodos soportados:**
  `GET` `POST` `DELETE`

* **Parámetros de datos (POST)**
**Requeridos:**<br>
  `name=[String]`<br>
  `username:[String]`<br>
  `email=[String]`<br>
  `address:[Dict]`<br>
  `phone=[String]`<br>
  `website=[String]`<br>
  `company=[Dict]`<br><br>

* **Respuesta:**
  
  En BD Local
  * **Código:** 201 <br>
  * **Contenido:** <br><br>
  
  ```
  {
    "id": 1,
    "name": "Camilo",
    "username": "cmantillam",
    "email": "manti@unal.edu.co",
    "address": {},
    "phone": "45678982",
    "website": "www.web.com",
    "company": {}
  }
  ``` 
  
  
 ### Consult

  Permite consultar los distintos servicios habilitados en JSONPlaceholder, adicionalmente permite guardar la consulta, clasificando los datos obtenidos para guardarlos de la manera adecuada en la BD local junto con sus relaciones requeridas. Por ejemplo, si se conultan posts, estos son creados por usuarios, por se busca el usuario, de confirma si existe, de no existir, se guarda también y finalmente, se guarda el post con su usuario asigando.
 
 * **URL:** <api/v1/consult/>
 
 * **Método:**
  `POST`

* **Parámetros de datos (POST)**
**Requeridos:**<br>
  `service=[String]` (Se señala el servicio que se quiere consumir en JSONPlaceholder)<br>
  `save_result=[Boolean]` (Se indica si se quieren guardar los objetos resultantes)<br><br>

* **Respuesta:**
  
  En BD Local
  * **Código:** 200 <br>
