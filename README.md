# biblioteca
Proyecto en python django para buscar y almacenar información, permitiendo la consulta a los APIs de Google books y Oreilly

## Instalación
Se descarga el proyecto, y se va a la ubicación del direcotrio principal, se utilizan los siguientes comandos:
```
git clone https://github.com/Jcmantillam/biblioteca.git
cd biblioteca
pip install -r requirements.txt
python manage.py migrate
```
## Servicios
Los servicios principales son el de búsqueda, guardar un libro y eliminar un libro. Adicionalmente, se puede utilizar le servicio ofrecido por Django Rest framework consultar los libros guardados, o crear un super usuario para Django Admin.  A continuación se explica cada servicio:

### Login API

  Este servicio permite buscar información de libros tanto en la BD local, como en los servicios externos soportados `GoogleBooks` y `Oreilly`
 
 * **URL:** <api/login>
 
 * **Método:**
  `POST`

* **Parámetros de datos**
**Requeridos:**<br>
  `username=[String]`<br>
  `password:[String]`<br><br>
 Con este método se obtiene el token de acceso a los demás endpoints del API.

* **Respuesta:**
  
  En BD Local
  * **Código:** 200 <br>
  * **Contenido:** <br><br>
  
  ```
  {
    "token": "5d76615727e04bbb0a95abd39498ee57c97bf4237"
  }
  ``` 

### Search Book

  Este servicio permite buscar información de libros tanto en la BD local, como en los servicios externos soportados `GoogleBooks` y `Oreilly`
 
 * **URL:** <api/v1/search_book/>
 
 * **Método:**
  `GET`

**Headers**

|**Name**|**Type**|**Description**|
|------|------|------|
| <center>Authorization</center> | <center>string</center>  | <center>Token String</center> |

* **Parámetros de datos**
**Requeridos:**<br>
  `search_term=[String]`<br>
  `alternative_service:[Char]`<br><br>
 `search_term` es el término buscado, mientras que `alternative_service` determina qué API externa se usará, G para Google y O para O'reilly<br>

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
  
  Con Google como alternativa
  * **Código:** 200 <br>
  * **Contenido:** <br><br>
  
  ```
  {
    "kind": "books#volumes",
    "totalItems": 522,
    "items": [
        {
            "kind": "books#volume",
            "id": "c6a2wgEACAAJ",
            "etag": "TPW/jYQQw4M",
            "selfLink": "https://www.googleapis.com/books/v1/volumes/c6a2wgEACAAJ",
            "volumeInfo": {
                "title": "Python Machine Learning: Aprendizaje automático y aprendizaje profundo con Python, scikit-learn y TesnorFlow",
                "industryIdentifiers": [
                    {
                        "type": "ISBN_10",
                        "identifier": "8426727204"
                    },
                    {
                        "type": "ISBN_13",
                        "identifier": "9788426727206"
                    }
                ],
                "readingModes": {
                    "text": false,
                    "image": false
                },
                "pageCount": 618,
                "printType": "BOOK",
                "maturityRating": "NOT_MATURE",
                "allowAnonLogging": false,
                "contentVersion": "preview-1.0.0",
                "panelizationSummary": {
                    "containsEpubBubbles": false,
                    "containsImageBubbles": false
                },
                "language": "es",
                "previewLink": "http://books.google.com.co/books?id=c6a2wgEACAAJ&dq=Python&hl=&cd=1&source=gbs_api",
                "infoLink": "http://books.google.com.co/books?id=c6a2wgEACAAJ&dq=Python&hl=&source=gbs_api",
                "canonicalVolumeLink": "https://books.google.com/books/about/Python_Machine_Learning_Aprendizaje_auto.html?hl=&id=c6a2wgEACAAJ"
            },
            "saleInfo": {
                "country": "CO",
                "saleability": "NOT_FOR_SALE",
                "isEbook": false
            },
            "accessInfo": {
                "country": "CO",
                "viewability": "NO_PAGES",
                "embeddable": false,
                "publicDomain": false,
                "textToSpeechPermission": "ALLOWED",
                "epub": {
                    "isAvailable": false
                },
                "pdf": {
                    "isAvailable": false
                },
                "webReaderLink": "http://play.google.com/books/reader?id=c6a2wgEACAAJ&hl=&printsec=frontcover&source=gbs_api",
                "accessViewStatus": "NONE",
                "quoteSharingAllowed": false
            },
            "save_link": "http://localhost:8000/api/v1/save_book/?book_id_g=c6a2wgEACAAJ"
        }
    ],
    "service": "G"
  ``` 
  
  Con O'reilly como alternativa
  * **Código:** 200 <br>
  * **Contenido:** <br><br>
  
  ```
  {
     {
    "results": [
        {
            "id": "https://www.safaribooksonline.com/api/v1/book/9780135917411/",
            "archive_id": "9780135917411",
            "ourn": "urn:orm:video:9780135917411",
            "last_modified_time": "2020-08-20T15:47:56.431Z",
            "issued": "2019-08-26T00:00:00Z",
            "format": "video",
            "content_format": "video",
            "authors": [
                "Paul J. Deitel"
            ],
            "publishers": [
                "Pearson"
            ],
            "academic_excluded": false,
            "language": "en",
            "title": "Python Fundamentals",
            "url": "https://learning.oreilly.com/api/v1/book/9780135917411/",
            "web_url": "/videos/python-fundamentals/9780135917411/",
            "source": "application/epub+zip",
            "content_type": "book",
            "duration_seconds": 162910,
            "video_classification": "course",
            "has_assessment": false,
            "timestamp": "2021-06-02T23:20:46.773Z",
            "description": "description",
            "average_rating": 4935,
            "number_of_followers": 0,
            "number_of_items": 0,
            "number_of_reviews": 31,
            "popularity": 999967990,
            "report_score": 153000,
            "cover_url": "https://learning.oreilly.com/library/cover/9780135917411/",
            "date_added": "2019-04-03T21:55:14.126Z",
            "topics": [
                "cda50ea0-3a3a-4d54-89bb-a7a4179365e6"
            ],
            "topics_payload": [
                {
                    "uuid": "cda50ea0-3a3a-4d54-89bb-a7a4179365e6",
                    "slug": "python",
                    "name": "Python",
                    "score": null
                }
            ],
            "save_link": "http://localhost:8000/api/v1/save_book/?book_id_o=9780135917411"
        }
  }

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
