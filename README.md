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

* **GET**

* **Parámetros de datos**
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
  * **Código:** 200 <br>
  * **Contenido:** <br><br>
  
  ```
  [
    {
        "id": 5,
        "title": "Python machine learning",
        "subtitle": "aprendizaje automático y aprendizaje profundo con Python, scikit-learn y TensorFlow",
        "release_date": "2019-01-01",
        "image": null,
        "description": "Not found",
        "editor": 5,
        "authors": [
            8,
            9
        ],
        "categories": [
            17
        ],
        "service": "local"
    }
  ]
  ``` 
  
  
 ### Save Book

  Este servicio está habilitado para guardar un resultado de la búsqueda externa seleccionada, sea `GoogleBooks` u `Oreilly`, como se puede observar, en los resultados de búsqueda anteriores, al final de los campos de cada libro, aparece un campo llamado `save_link`, este campo facilita el vínculo para realizar el guardado  del libro al cual pertenece en la BD local.
 
 * **URL:** <api/v1/save_book/>
 
 * **Método:**
  `POST`
 
 **Headers**

|**Name**|**Type**|**Description**|
|------|------|------|
| <center>Authorization</center> | <center>string</center>  | <center>Token String</center> |

* **Parámetros en URL**
**Requeridos:**<br>
  `?book_id_g=:[String]`<br>
  `?book_id_o=:[String]`<br><br>
 `?book_id_g=` es para guardar un libro encontrado en el API de Google, mientras que `?book_id_o=` es para guardar un libro del API de Oreilly<br>

* **Respuesta:**
  
  En BD Local
  * **Código:** 201 <br>

### Delete Book

  Con este servicio se puede eliminar un libro de la BD local.
 
 * **URL:** <api/v1/delete_book/>
 
 * **Método:**
  `POST`

**Headers**

|**Name**|**Type**|**Description**|
|------|------|------|
| <center>Authorization</center> | <center>string</center>  | <center>Token String</center> |

* **Parámetros de datos**
**Requeridos:**<br>
  `id=[integer]`<br><br>
 `id` es el id del libro que se desea eliminar.<br>

* **Respuesta:**
  
  En BD Local
  * **Código:** 200 <br>
