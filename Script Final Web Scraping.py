#-------------------------------------------------------------------------------------------------------------------
#Scrapping de los encurtidos de ajo
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Seleccion", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Ingles", "Special Line", "Aliada", "Hipercor", "Veckia"
    ]

url = 'https://soysuper.com/c/aperitivos/encurtidos/ajo/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 1 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrappping de los encurtidos de alcaparras

import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/aperitivos/encurtidos/alcaparras/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 2 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de los encurtidos de banderillas       
       
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/aperitivos/encurtidos/banderillas/t/marca-blanca/picantes#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 3 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de los encurtidos de cebollitas 
         
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/aperitivos/encurtidos/cebollitas/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 4 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

 #--------------------------------------------------------------------------------------------------------------
 # scrapping de los encurtidos de coctel
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/aperitivos/encurtidos/coctel/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 5 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")
        
#--------------------------------------------------------------------------------------------------------------
# scrapping de los encurtidos de pepinillos
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/aperitivos/encurtidos/pepinillos/t/marca-blanca#products'
page = 1

# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()

# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()

        # Verificar si el nombre del producto contiene "pepinillos pequeños"
        if "pepinillos pequeños" not in product_name.lower():
            continue

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 6, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")  

#--------------------------------------------------------------------------------------------------------------
# scrapping de los snacks de cintas de maiz
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/aperitivos/snacks/cintas/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 7 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")
        
#--------------------------------------------------------------------------------------------------------------
# scrapping de los snacks de conos de maiz
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/aperitivos/snacks/conos/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 8 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")
 
#--------------------------------------------------------------------------------------------------------------
# scrapping de los snacks de torreznos de cerdo
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/aperitivos/snacks/cortezas-y-torreznos/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()

        # Verificar si el nombre del producto contiene "torreznos"
        if "torreznos" not in product_name.lower():
            continue

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 9 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de los snacks de coctel
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/aperitivos/snacks/cocteles/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 10 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de los snacks de galletas saladas
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/aperitivos/snacks/galletas-saladas/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()

        # Verificar si el nombre del producto contiene "galletitas saladas"
        if "galletitas saladas" not in product_name.lower():
            continue

        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 11 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de los snacks de gusanitos de maiz
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/aperitivos/snacks/gusanitos/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 12 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de los snacks de nachos de maiz
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/aperitivos/snacks/nachos/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Verificar si el nombre del producto contiene "tex-mex"
        if "tex mex" not in product_name.lower():
            continue

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 13 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de los snacks de palomitas de maíz
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/aperitivos/snacks/palomitas/t/marca-blanca/para-microondas#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Verificar si el nombre del producto contiene "mantequilla"
        if "mantequilla" not in product_name.lower():
            continue

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 14 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de los snacks tortitas de arroz
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/aperitivos/snacks/tortitas/t/con-chocolate/de-arroz/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Verificar si el nombre del producto contiene "chocolate"
        if "chocolate" not in product_name.lower():
            continue

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 15 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de las aceitunas negras con hueso
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/aperitivos/aceitunas/negras/t/con-hueso/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Verificar si el nombre del producto contiene "con hueso"
        if "con hueso" not in product_name.lower():
            continue

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 16 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de las aceitunas negras sin hueso
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/aperitivos/aceitunas/negras/t/marca-blanca/sin-hueso#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 17 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de las aceitunas verdes de anchoa
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/aperitivos/aceitunas/t/de-anchoa/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()
        
         # Verificar si el tamaño del producto contiene "3 und x 50 g"
        if "3 uds x 50 g" not in tamanio.lower():
            continue

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 18 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de las aceitunas verdes rellanas de pimiento
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/aperitivos/aceitunas/t/de-pimiento/marca-blanca/rellenas#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()
        
         # Verificar si el tamaño del producto contiene "150 g"
        if "150 g" not in tamanio.lower():
            continue

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 19 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de las aceitunas verdes gordal Con Hueso
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/aperitivos/aceitunas/t/con-hueso/gordal/marca-blanca/m/el-corte-ingles#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Verificar si el nombre del producto contiene "grodal con hueso"
        if "gordal" not in product_name.lower():
            continue

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 20 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de las aceitunas verdes manzanillas con hueso
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/aperitivos/aceitunas/t/con-hueso/manzanilla/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 21 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de las aceitunas verdes manzanillas sin hueso
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/aperitivos/aceitunas/t/manzanilla/marca-blanca/sin-hueso#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
          # Verificar si el tamaño del producto contiene "400g"
        if "400 g" not in tamanio.lower():
            continue

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 22 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de las aceitunas aliñadas
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/aperitivos/aceitunas/t/alinadas/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Verificar si el nombre del producto contiene "aliñadas"
        if "aliñada" not in product_name.lower():
            continue

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 23 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping del aceite de girasol de 1 litro
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/aceite/de-girasol/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Verificar si el tamaño del producto contiene "1l" o "1 l"
        if "1 l" not in tamanio.lower():
            continue


        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 24 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping del aceite de girasol de 5 litros
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/aceite/de-girasol/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Verificar si el tamaño del producto contiene "1l" o "1 l"
        if "5 l" not in tamanio.lower():
            continue


        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 25 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")
                   
# --------------------------------------------------------------------------------------------------------------
# scrapping del aceite de oliva sabor intenso de 1 litro
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/aceite/de-oliva/t/marca-blanca/sabor-intenso#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Verificar si el tamaño del producto contiene "1l" o "1 l"
        if "1 l" not in tamanio.lower():
            continue


        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 26 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping del aceite de oliva sabor suave de 1 litro
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/aceite/de-oliva/t/marca-blanca/sabor-suave#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Verificar si el tamaño del producto contiene "1l" o "1 l"
        if "1 l" not in tamanio.lower():
            continue


        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 27 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping del aceite de oliva virgen extra de 1 litro
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/aceite/de-oliva/t/marca-blanca/virgen-extra#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Verificar si el tamaño del producto contiene "1l" o "1 l"
        if "1 l" not in tamanio.lower():
            continue


        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 26 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping del arroz blanco bomba de 1 kilo
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/pasta-arroz-y-legumbres/arroz/blanco/t/bomba/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 29 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping del arroz blanco largo de 1 kilo
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/pasta-arroz-y-legumbres/arroz/blanco/t/largo/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
         # Verificar si el nombre del producto no contiene "vaporizado"
        if "vaporizado" in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 30 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping del arroz blanco bomba de 1 kilo
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/pasta-arroz-y-legumbres/arroz/blanco/t/marca-blanca/redondo#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
         # Verificar si el nombre del producto no contiene "bomba"
        if "bomba" in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 31 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping del arroz blanco vaporizado de 1 kilo
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/pasta-arroz-y-legumbres/arroz/blanco/t/marca-blanca/vaporizado#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 32 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping del arroz integral de 1 kilo
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/pasta-arroz-y-legumbres/arroz/integral/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 33 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping del azucar blanco de 1 kilo
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/panaderia-pasteleria-y-reposteria/azucar-y-edulcorantes/azucar/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
         # Verificar si el nombre del producto contiene "blanco"
        if "blanca" not in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 31 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping del azucar moreno de 1 kilo
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/panaderia-pasteleria-y-reposteria/azucar-y-edulcorantes/azucar/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
         # Verificar si el nombre del producto contiene "moreno"
        if "moreno" not in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 36 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping del sacarina
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/panaderia-pasteleria-y-reposteria/azucar-y-edulcorantes/edulcorante/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
         # Verificar si el nombre del producto contiene "edulcorante liquido"
        if "edulcorante líquido" not in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 37 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de stevia
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/panaderia-pasteleria-y-reposteria/azucar-y-edulcorantes/edulcorante/t/marca-blanca/stevia#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 38 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de agua con gas
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/bebidas/agua/con-gas/t/marca-blanca/m/aguadoy/aliada/carrefour/dia/el-corte-ingles/producto-alcampo#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "1,5 l" not in tamanio.lower():
            continue
        

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 39, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de agua sin gas
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/bebidas/agua/sin-gas/t/marca-blanca/m/aguadoy/aliada/carrefour/dia/el-corte-ingles/producto-alcampo#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "1,5 l" not in tamanio.lower():
            continue
        

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 40, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de cerveza nacional
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/bebidas/cerveza/nacional/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "12 latas" not in tamanio.lower():
            continue
        

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 41, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de cerveza sin alcohol
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/bebidas/cerveza/sin-alcohol/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "con limon" in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "33 cl" not in tamanio.lower():
            continue
        

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 42, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de bebidas de refrescos de cola
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/bebidas/refresco/cola/t/marca-blanca/m/el-corte-ingles#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "sin azúcares" in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "2 l" not in tamanio.lower():
            continue
        

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 43, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")
#--------------------------------------------------------------------------------------------------------------
# scrapping de bebidas de refrescos de lima- limon
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/bebidas/refresco/lima-limon/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "lima limon" not in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "2 l" not in tamanio.lower():
            continue
        

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 45, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de bebidas de refrescos de naranja
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/bebidas/refresco/naranja/t/con-gas/marca-blanca/m/#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "zero" in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "2 l" not in tamanio.lower():
            continue
        

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 46, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de bebidas de refrescos te frio
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/bebidas/refresco/te/t/al-limon/marca-blanca/#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "zero" in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "1.5 l" not in tamanio.lower():
            continue
        

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 47, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de bebidas de zumos con leche
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/bebidas/zumo/con-leche/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "mediteraneo" not in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "200 ml" not in tamanio.lower():
            continue
        

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 48, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de bebidas de zumos de manzana
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/bebidas/zumo/manzana/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "zumo" not in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "1 l" not in tamanio.lower():
            continue
        

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 49, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")
#--------------------------------------------------------------------------------------------------------------
# scrapping de bebidas de zumos de melocoton y uva
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/bebidas/zumo/mezcla-de-frutas/t/marca-blanca/melocoton/uva#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "zumo" not in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "1 l" not in tamanio.lower():
            continue
        

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 50, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de bebidas de zumos de naranja
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/bebidas/zumo/naranja/t/marca-blanca/zumo#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "zumo" not in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "1 l" not in tamanio.lower():
            continue
        

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 51, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de bebidas de zumos de piña y uva
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/bebidas/zumo/mezcla-de-frutas/t/marca-blanca/pina/uva#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
       
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "200 ml" not in tamanio.lower():
            continue
        

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 52, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de cafes en capsulas descafeinados
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/cafes-cacaos-e-infusiones/cafe/capsulas/t/descafeinado/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "compatible" in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 53, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de cafes en capsulas de cafe intenso
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/cafes-cacaos-e-infusiones/cafe/capsulas/t/intenso/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "30 uds." not in tamanio.lower():
            continue
        

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 54, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de cafes en capsulas de cafe expresso
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/cafes-cacaos-e-infusiones/cafe/capsulas/t/expresso/marca-blanca/m/dia#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 55 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de cafes en capsulas de cafe con leche
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/cafes-cacaos-e-infusiones/cafe/capsulas/t/con-leche/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "10" in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 56, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de cafes descafeinado molido
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/cafes-cacaos-e-infusiones/cafe/descafeinado/t/marca-blanca/molido#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
         # Verificar si el tamaño del producto contiene "1.5 l"
        if "natural" not in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "200 g" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 57, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")


#--------------------------------------------------------------------------------------------------------------
# scrapping de cafes descafeinado soluble
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/cafes-cacaos-e-infusiones/cafe/descafeinado/t/marca-blanca/soluble#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "200 g" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 58, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")


#--------------------------------------------------------------------------------------------------------------
# scrapping de cafes soluble cappucchino
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/cafes-cacaos-e-infusiones/cafe/soluble/t/cappuccino/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "cappuccino" not in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "200 g" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 59, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")


#--------------------------------------------------------------------------------------------------------------
# scrapping de cafes soluble natural
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/cafes-cacaos-e-infusiones/cafe/soluble/t/marca-blanca/natural#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "200 g" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 60, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")


#--------------------------------------------------------------------------------------------------------------
# scrapping de bacon en lonchas
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/frescos-y-charcuteria/charcuteria/bacon-y-panceta/t/bacon/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "en lonchas" not in product_name.lower():
            continue
    
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 61, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de bacon en tacos
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/frescos-y-charcuteria/charcuteria/bacon-y-panceta/t/bacon/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "tiras" not in product_name.lower():
            continue
    
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 62, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de chorizo en lonchas
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/frescos-y-charcuteria/charcuteria/chorizo/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "pamplona extra" not in product_name.lower():
            continue
    
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 63, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de chorizo pieza
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/frescos-y-charcuteria/charcuteria/chorizo/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "dulce extra" not in product_name.lower():
            continue
    
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 64, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de fuet
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/frescos-y-charcuteria/charcuteria/fuet-longaniza/t/fuet/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "fuet" not in product_name.lower():
            continue
    
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 65, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de longaniza
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/frescos-y-charcuteria/charcuteria/fuet-longaniza/t/longaniza/marca-blanca/m/el-corte-ingles#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "extra" not in product_name.lower():
            continue
    
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 66, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de jamon cocido en lonchas
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/frescos-y-charcuteria/charcuteria/jamon-cocido/t/en-lonchas/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "finas" in product_name.lower():
            continue
    
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 67, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de jamon cocido en lonchas finas
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/frescos-y-charcuteria/charcuteria/jamon-cocido/t/en-lonchas/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "finas" not in product_name.lower():
            continue
    
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "150 g" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 69, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de jamon curado serrano en lonchas
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Mercadona", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Economicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/frescos-y-charcuteria/charcuteria/jamon-curado/t/en-lonchas/marca-blanca/serrano#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 69 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
 # scrapping de jamon curado iberico en lonchas
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/frescos-y-charcuteria/charcuteria/jamon-curado/t/en-lonchas/iberico/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Verificar si el tamaño del producto contiene "1.5 l"
        if "ibérico" not in product_name.lower():
            continue
    
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 70, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de lomo embuchado en lonchas
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/frescos-y-charcuteria/charcuteria/lomo/t/marca-blanca/m/carrefour#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
         # Verificar si el tamaño del producto contiene "1.5 l"
        if "embuchado" not in product_name.lower():
            continue
    
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 71, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de lomo en pieza embuchado
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/frescos-y-charcuteria/charcuteria/lomo/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
    
        if "pieza" not in product_name.lower():
            continue
        
        if "cabecero" in product_name.lower():
            continue
    
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 72, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de mortadela en lonchas
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/frescos-y-charcuteria/charcuteria/mortadela/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
    
        if "lonchas" not in product_name.lower():
            continue
    
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 73, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de salchicha frankfurt
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/frescos-y-charcuteria/charcuteria/salchichas-envasadas/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "frankfurt" not in product_name.lower():
            continue
        
        if "queso" in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 74, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de salchicha frankfurt con queso
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/frescos-y-charcuteria/charcuteria/salchichas-envasadas/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "frankfurt" not in product_name.lower():
            continue
        
        if "queso" not in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 74, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de salchicha de pavo
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/frescos-y-charcuteria/charcuteria/salchichas-envasadas/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "pavo" not in product_name.lower():
            continue
        
        if "queso" in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 76, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de salchichon en lonchas
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/frescos-y-charcuteria/charcuteria/salchichon/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "extra" not in product_name.lower():
            continue
        
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 77, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de salchichon en finas lonchas
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/frescos-y-charcuteria/charcuteria/salchichon/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "finas lonchas" not in product_name.lower():
            continue
        
        if "pieza" in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 78, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de canela en polvo
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/especias/canela/t/molida#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 79 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")



# --------------------------------------------------------------------------------------------------------------
# scrapping de canela en rama
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/especias/canela/t/en-rama#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 80 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")


# --------------------------------------------------------------------------------------------------------------
# scrapping de ajo seco en polvo
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/especias/ajo-seco/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 81 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")


# --------------------------------------------------------------------------------------------------------------
# scrapping de albahaca seca
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/especias/albahaca/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 82 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")


#--------------------------------------------------------------------------------------------------------------
# scrapping de cebolla seca en polvo
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/especias/cebolla/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 83 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")


#--------------------------------------------------------------------------------------------------------------
# scrapping de comino en polvo
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/especias/comino/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 84 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")


#--------------------------------------------------------------------------------------------------------------
# scrapping de curry en polvo
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/especias/curry/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 85 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")


#--------------------------------------------------------------------------------------------------------------
# scrapping de curcuma
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/especias/curcuma/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 86 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")


#--------------------------------------------------------------------------------------------------------------
# scrapping de eneldo seco
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/especias/eneldo/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 87 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")


#--------------------------------------------------------------------------------------------------------------
# scrapping de jengibre seco en polvo
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/especias/jengibre/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 88 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")


#--------------------------------------------------------------------------------------------------------------
# scrapping de laurel seco en hojas
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/especias/laurel/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 89 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")


#--------------------------------------------------------------------------------------------------------------
# scrapping de nuez moscada seca en polvo
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/especias/nuez-moscada/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 90 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")


#--------------------------------------------------------------------------------------------------------------
# scrapping de oregano seco
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/especias/oregano/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 91 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")


#--------------------------------------------------------------------------------------------------------------
# scrapping de perejil seco
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/especias/perejil/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 92 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")


#--------------------------------------------------------------------------------------------------------------
# scrapping de tomillo seco
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/especias/tomillo/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 93 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de pimenta negra seca en grano
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/especias/pimienta/t/en-grano/marca-blanca/negra#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 94 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de pimenta negra seca molida
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/especias/pimienta/t/marca-blanca/molida/negra#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 95 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de sal fina
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/especias/sal/t/fina/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "mesa" in product_name.lower():
            continue
        
        if "yodada" in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 96, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de sal gorda
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/especias/sal/t/gruesa/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 97 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de salsa ketuchup
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/salsas/ketchup/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "monodosis" in product_name.lower():
            continue
        
        if "zero" in product_name.lower():
            continue
        
        if "light" in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "6" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 98, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de salsa mayonesa
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/salsas/mayonesa/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "suave" in product_name.lower():
            continue
        
        if "ligera" in product_name.lower():
            continue
        
        if "light" in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "5" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 99, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de salsa mostaza
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/salsas/mostaza/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "miel" in product_name.lower():
            continue
        
        if "dijon" in product_name.lower():
            continue
        
        if "granitos" in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 100, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de tomate frito
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/salsas/tomate-frito/t/marca-blanca/#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "artesana" in product_name.lower():
            continue
        
        if "oliva" in product_name.lower():
            continue
        
        if "abuela" in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
       
        if "frasco de 560" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 101, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de vinagre balsamico
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/vinagre/balsamico/t/de-modena/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 102 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de vinagre de jerez
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/vinagre/de-jerez/t/marca-blanca/m/carrefour#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "crema" in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        if "50 ml" not in tamanio.lower():
            continue

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 103 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de vinagre de manzana
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/vinagre/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "de manzana" not in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 104 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de atún al natural
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/conservas-de-pescado/atun/t/al-natural/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
       
        if "6 latas" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 105, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de atún en aceite de girasol
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/conservas-de-pescado/atun/t/de-girasol/marca-blanca/m/hacendado#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
       
        if "pack 6" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 106, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")


#--------------------------------------------------------------------------------------------------------------
# scrapping de atún en aceite de oliva
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/conservas-de-pescado/atun/t/en-aceite-de-oliva/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
       
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
       
        if "6 latas" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 107, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de bonito del norte en aceite de oliva
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/conservas-de-pescado/bonito-del-norte/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
       
        if "260" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 108, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de bonito del norte en escabeche
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/conservas-de-pescado/bonito-del-norte/t/en-escabeche/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
       
        if "73" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 110, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de sardinas en aceite de oliva
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/conservas-de-pescado/sardinas/t/en-aceite-de-oliva/marca-blanca/m/mari-marinera#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
       
        if "85" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 110, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de sardinas en tomate
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/conservas-de-pescado/sardinas/t/con-tomate/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
       
        if "85" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 111, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de mermelada de albaricoque
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/conservas-dulces/confituras-y-mermeladas/t/albaricoque/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
       
        if "410" not in tamanio.lower():
            continue
        
       
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 112, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de mermelada de ciruela
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/conservas-dulces/confituras-y-mermeladas/t/ciruela/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
       
        if "310" not in tamanio.lower():
            continue
        
       
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 113, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de mermelada de fresa
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/conservas-dulces/confituras-y-mermeladas/t/fresa/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
       
        if "410" not in tamanio.lower():
            continue
        
       
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 114, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de mermelada de melocotón
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/conservas-dulces/confituras-y-mermeladas/t/marca-blanca/melocoton#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
       
        if "410" not in tamanio.lower():
            continue
        
       
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 115, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de miel de 500g
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/conservas-dulces/miel/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
       
        if "500 g" not in tamanio.lower():
            continue
        
       
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 116, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de miel de 1kg
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/conservas-sopas-aceites-y-condimentos/conservas-dulces/miel/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
       
        if "1 kg" not in tamanio.lower():
            continue
        
       
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 117, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de body milk de 500ml
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/perfumeria-y-parafarmacia/cuidado-corporal/cremas-y-lociones/t/body-milk/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 118 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de corporal
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/perfumeria-y-parafarmacia/cuidado-corporal/cremas-y-lociones/t/crema-corporal/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "oliva" not in product_name.lower():
            continue
           
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
    
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 119, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de gel de baño 
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/perfumeria-y-parafarmacia/cuidado-corporal/cremas-y-lociones/t/gel-corporal/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "miel" not in product_name.lower():
            continue
           
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
    
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 120, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de loción corporal
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/perfumeria-y-parafarmacia/cuidado-corporal/cremas-y-lociones/t/locion-corporal/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "aloe" not in product_name.lower():
            continue
           
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
    
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 121, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping jabon de manos en pastilla
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/perfumeria-y-parafarmacia/cuidado-corporal/jabon-para-manos/t/marca-blanca/pastilla/m/deliplus/les-cosmetiques#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        
           
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
    
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 122, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")


# --------------------------------------------------------------------------------------------------------------
# scrapping de jabon de manos liquido
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/perfumeria-y-parafarmacia/cuidado-corporal/jabon-para-manos/t/liquido/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "avena" not in product_name.lower():
            continue
           
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
    
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 123, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de detergente en polvo
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/drogueria/cuidado-de-la-ropa/detergente/t/en-polvo/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        
           
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
    
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 124, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de detergente liquido para lavadora
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/drogueria/cuidado-de-la-ropa/detergente/t/con-jabon-de-marsella/liquido/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "flor"  in product_name.lower():
            continue
           
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "46" not in tamanio.lower():
            continue
    
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 125, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de quitamanchas en polvo
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/drogueria/cuidado-de-la-ropa/quitamanchas/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "flor"  in product_name.lower():
            continue
           
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "1 kg" not in tamanio.lower():
            continue
    
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 126, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de quitamanchas en spray
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/drogueria/cuidado-de-la-ropa/quitamanchas/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
    
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()
        
        if "oxy" not in product_name.lower():
            continue

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "500 ml" not in tamanio.lower():
            continue
    
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 127, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de suavizante para la ropa azul
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/drogueria/cuidado-de-la-ropa/suavizante/t/concentrado/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
    
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()
        
        if "azul" not in product_name.lower():
            continue

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 128, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de suavizante para la ropa talco
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/drogueria/cuidado-de-la-ropa/suavizante/t/concentrado/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
    
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()
        
        if "talco" not in product_name.lower():
            continue

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 129, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de legumbres cocidas alubias blancas
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/pasta-arroz-y-legumbres/legumbres-cocidas/alubias-cocidas/t/blancas/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
    
        if "judion" in product_name.lower():
            continue
    
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "400 g" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 130, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de legumbres cocidas alubias rojas
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/pasta-arroz-y-legumbres/legumbres-cocidas/alubias-cocidas/t/marca-blanca/rojas#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 131 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de legumbres cocidas garbanzos cocidos
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/pasta-arroz-y-legumbres/legumbres-cocidas/garbanzos-cocidos/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
    
        if "verduras" in product_name.lower():
            continue
        
        if "sal" in product_name.lower():
            continue
        
        if "pedrosillano" in product_name.lower():
            continue
    
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "400 g" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 132, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de legumbres cocidas judión
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/pasta-arroz-y-legumbres/legumbres-cocidas/alubias-cocidas/t/judion/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 133 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de legumbres cocidas lentejas cocidas
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/pasta-arroz-y-legumbres/legumbres-cocidas/lentejas-cocidas/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
    
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "400 g" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 134, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de legumbres secas alubias blancas
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/pasta-arroz-y-legumbres/legumbres-secas/alubias/t/blancas/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
    
        if "judión" in product_name.lower():
            continue
        
        if "riñón" in product_name.lower():
            continue
        
        if "fabada" in product_name.lower():
            continue
    

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "1 kg" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 135, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de legumbres secas alubias rojas
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/pasta-arroz-y-legumbres/legumbres-secas/alubias/t/marca-blanca/pintas#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
    
        if "canela" in product_name.lower():
            continue
        
        if "castilla" in product_name.lower():
            continue
        
        if "extra de nuestra" in product_name.lower():
            continue
    

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "1 kg" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 136, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de legumbres secas alubias negras
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/pasta-arroz-y-legumbres/legumbres-secas/alubias/t/marca-blanca/negras#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 137 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de legumbres secas garbanzos
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/pasta-arroz-y-legumbres/legumbres-secas/garbanzos/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
    
        if "lechoso" in product_name.lower():
            continue
        
        if "sal" in product_name.lower():
            continue
        
        if "pedrosillano" in product_name.lower():
            continue
    

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "1 kg" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 138, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de legumbres secas lentejas
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/pasta-arroz-y-legumbres/legumbres-secas/lentejas/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "extra" not in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "1 kg" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 139, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de legumbres secas lentejas pardinas
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/pasta-arroz-y-legumbres/legumbres-secas/lentejas/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "pard" not in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "1 kg" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 140, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de huevos talla L
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Huevos Guillén", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/lacteos-y-huevos/huevos/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "clase l" not in product_name.lower():
            continue
        
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "12" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 141, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de huevos talla M
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Huevos Guillén", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/lacteos-y-huevos/huevos/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "clase m" not in product_name.lower():
            continue
        
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "12 u" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 142, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de huevos talla XL
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Huevos Guillén", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/lacteos-y-huevos/huevos/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "xl" not in product_name.lower():
            continue
        
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "12" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 143, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de leche desnatada
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/lacteos-y-huevos/leche/desnatada/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "calcio" in product_name.lower():
            continue
        
        if "lact" in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "1 l" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 144, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de leche entera
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/lacteos-y-huevos/leche/entera/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "6" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 145, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de leche semidesnatada
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/lacteos-y-huevos/leche/semidesnatada/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "calcio" in product_name.lower(): 
            continue
        
        if "lactosa" in product_name.lower(): 
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "6" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 147, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de leche sin lactosa
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/lacteos-y-huevos/leche/sin-lactosa/t/marca-blanca/semidesnatada#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "semidesnatada" not in product_name.lower(): 
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "6 x 1 l" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 147, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de mantequilla con sal
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/lacteos-y-huevos/mantequilla/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "con sal" not in product_name.lower(): 
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "250" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 148, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de mantequilla sin sal
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/lacteos-y-huevos/mantequilla/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "sin sal" not in product_name.lower(): 
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "pastilla 250" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 149, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de margarina con sal
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/lacteos-y-huevos/margarina/t/con-sal/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "con sal" not in product_name.lower(): 
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "500" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 150, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de margarina sin sal
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/lacteos-y-huevos/margarina/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "con" in product_name.lower(): 
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "500" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 151, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de nata montada
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/lacteos-y-huevos/nata/montada/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "ligera" in product_name.lower(): 
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "250" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 152, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de nata para cocinar
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/lacteos-y-huevos/nata/para-cocinar/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "3" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 153, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de nata para montar
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/lacteos-y-huevos/nata/para-montar/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "3" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 154, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de amoniaco perfumado
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/drogueria/limpieza-del-hogar/lejia-y-liquidos-fuertes/t/amoniaco/marca-blanca/m/bosque-verde/carrefour/dia/producto-alcampo#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "perfumado" not in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "1.5" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 155, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")
# --------------------------------------------------------------------------------------------------------------
# scrapping de lejia pura
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/drogueria/limpieza-del-hogar/lejia-y-liquidos-fuertes/t/lejia/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "detergente" in product_name.lower():
            continue
        
        if "perfumado" in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "2" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 156, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de lejia con detergente
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/drogueria/limpieza-del-hogar/lejia-y-liquidos-fuertes/t/con-detergente/lejia/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "limón" in product_name.lower():
            continue
        
        if "pino" in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "2" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 157, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de lejia perfumada
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/drogueria/limpieza-del-hogar/lejia-y-liquidos-fuertes/t/lejia/marca-blanca/perfumada#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "perfumada" not in product_name.lower():
            continue

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "2" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 158, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de abrillantador de lavavajllas
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/drogueria/lavavajillas/abrillantador-lavavajillas/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 159 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de liquido lavavajillas a mano
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/drogueria/lavavajillas/detergente-lavavajillas/t/a-mano/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "verde" not in product_name.lower():
            continue

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "1 l" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 160, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de limpia induccion
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/drogueria/limpieza-de-la-cocina/limpieza-de-electrodomesticos/t/limpieza-de-vitroceramicas/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "inducción" not in product_name.lower():
            continue

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "500" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 161, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de limpia vitroceramica
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/drogueria/limpieza-de-la-cocina/limpieza-de-electrodomesticos/t/limpieza-de-vitroceramicas/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "vitro" not in product_name.lower():
            continue

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "500" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 162, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de pastillas de lavavajillas
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/drogueria/lavavajillas/t/marca-blanca/pastilla#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "todo en 1" not in product_name.lower():
            continue

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 163, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de friegasuelos concentrado
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/drogueria/limpieza-del-hogar/limpiasuelos/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "concentrado" not in product_name.lower():
            continue

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 164, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de friegasuelos flor de cerezo
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/drogueria/limpieza-del-hogar/limpiasuelos/t/marca-blanca/m/bosque-verde/carrefour#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "flor de" not in product_name.lower():
            continue

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 165, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de friegasuelos pino
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/drogueria/limpieza-del-hogar/limpiasuelos/t/marca-blanca/m/bosque-verde/carrefour/producto-alcampo#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "pino" not in product_name.lower():
            continue

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 166, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de friegasuelos spa
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/drogueria/limpieza-del-hogar/limpiasuelos/t/marca-blanca/m/bosque-verde/carrefour/producto-alcampo#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "spa" not in product_name.lower():
            continue

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 167, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de papel higienico 2 capa
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/drogueria/celulosa/papel-higienico/t/blanco/dos-capas/marca-blanca/m/bosque-verde/carrefour/producto-alcampo#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "confort" in product_name.lower():
            continue

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "12" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 168, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de papel higienico 3 capa
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/drogueria/celulosa/papel-higienico/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "3 capas" not in product_name.lower():
            continue

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "12" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 169, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de papel higienico 4 capa
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/drogueria/celulosa/papel-higienico/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "4 capas" not in product_name.lower():
            continue

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
       
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 170, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de papel de cocina 3 rollos
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/drogueria/celulosa/papel-de-cocina/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "gigante" in product_name.lower():
            continue

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "3" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 171, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de papel de cocina maxi
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/drogueria/celulosa/papel-de-cocina/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "jumbo" in product_name.lower():
            continue

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "1" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 172, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de pañuelos blancos
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/drogueria/celulosa/panuelos/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "blancos" not in product_name.lower():
            continue

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "10" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 173, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de pañuelos mentolados
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/drogueria/celulosa/panuelos/t/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "mentol" not in product_name.lower():
            continue

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "10" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 174, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
#scrapping de queso fresco de burgos
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/frescos-y-charcuteria/queso/fresco-y-para-ensaladas/t/marca-blanca/m/aliada#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "burgos" not in product_name.lower():
            continue

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "250 g" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 175, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de queso para ensaladas
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/frescos-y-charcuteria/queso/fresco-y-para-ensaladas/t/marca-blanca/para-ensaladas#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 176 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de queso fundido en lonchas
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/frescos-y-charcuteria/queso/lonchas-rallado-y-en-porciones/t/en-lonchas/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "fundido" not in product_name.lower():
            continue

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
       
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 177, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de queso en locnhas gouda
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/frescos-y-charcuteria/queso/lonchas-rallado-y-en-porciones/t/gouda/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "lonchas" not in product_name.lower():
            continue

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
       
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 178, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de queso en lonchas havarti
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/frescos-y-charcuteria/queso/lonchas-rallado-y-en-porciones/t/marca-blancao#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        if "havarti lonchas" not in product_name.lower():
            continue

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
       
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 179, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

# --------------------------------------------------------------------------------------------------------------
# scrapping de queso en lonchas cheddar
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/frescos-y-charcuteria/queso/lonchas-rallado-y-en-porciones/t/cheddar/marca-blanca#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 180 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de queso rallado mozarella
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/frescos-y-charcuteria/queso/lonchas-rallado-y-en-porciones/t/marca-blanca/mozzarella/rallado#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
       

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        if "200" not in tamanio.lower():
            continue
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 181, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de queso rallado emmental
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/frescos-y-charcuteria/queso/lonchas-rallado-y-en-porciones/t/emmental/marca-blanca/rallado#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 182 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de queso rallado parmesano
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/frescos-y-charcuteria/queso/lonchas-rallado-y-en-porciones/t/grana-padano/marca-blanca/rallado#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 183 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de queso rallado 4 quesos
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/frescos-y-charcuteria/queso/lonchas-rallado-y-en-porciones/t/marca-blanca/rallado#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
       
        if "4 quesos" not in product_name.lower():
            continue

        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 184, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de queso rallado para fundir
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/frescos-y-charcuteria/queso/lonchas-rallado-y-en-porciones/t/marca-blanca/para-fundir-y-gratinar/rallado#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 185 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de queso mozzarella en lonchas
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour BIO",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/frescos-y-charcuteria/queso/mozzarella-parmesano-y-ricotta/t/en-lonchas/marca-blanca/mozzarella#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip()

        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 186 , 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------
# scrapping de queso mozzarella fresca
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Lista de marcas
brands = [
    "Hacendado", "Deliplus", "Bosque Verde", "Compy", "Aguadoy", "Steinburg", "Cason Historico", "Delikuit",
    "Krislin", "Nuske", "Huerta de barros", "Huevos Guillen", "Alitey", "Sun Med", "Producto Alcampo", "Alcampo",
    "Alcampo Gourmet", "Productos Económicos Alcampo", "Cosmia", "Heifer", "SNC", "DIA", "Bonte", "Baby Smile",
    "DIA Vital", "DIA Delicious", "AS", "Mari Marinera", "DIA LA LLAMA", "Carrefour", "Carrefour Bio",
    "Carrefour Selección", "Simpl", "De Nuestra Tierra", "Carrefour Kids", "Carrefour Baby", "Carrefour Home",
    "Les Cosmétiques", "El Corte Inglés", "Special Line", "Aliada", "Hipercor", "Veckia"
]

url = 'https://soysuper.com/c/frescos-y-charcuteria/queso/mozzarella-parmesano-y-ricotta/t/fresca/marca-blanca/mozzarella#products'
page = 1


# Conectar a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="vsantiab",
  password="root",
  database="bbdd_proyecto_final"
)

# Crear un objeto cursor para realizar operaciones SQL
cursor = db.cursor()


# Lista para almacenar los productos ya agregados
added_products = []

max_pages = 10

while page <= max_pages:
    # Realizar la solicitud HTTP y obtener el HTML de la página
    response = requests.get(url)
    html = response.content

    # Crear un objeto BeautifulSoup a partir del HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar la lista de productos
    product_list = soup.find('ul', {'class': 'basiclist productlist grid clearfix'})

    # Si no se encuentra la lista de productos, significa que hemos llegado al final de las páginas
    if not product_list:
        break

    # Encontrar todos los productos en la lista
    products = product_list.find_all('li')

    # Iterar sobre los productos y extraer la información relevante
    for product in products:
        # Extraer nombre del producto
        product_name = product.find('span', {'class': 'productname'})
        if product_name is None:
            continue
        product_name = product_name.text.strip()
       
        if "fresca" not in product_name.lower():
            continue
        
        # Extraer marca
        brand = product.find('span', {'class': 'brand'})
        if brand is None:
            continue
        brand = brand.text.strip()   

        # Filtrar por marcas específicas
        if brand not in brands:
            continue

        # Extraer precio
        price = product.find('meta', {'itemprop': 'price'})
        if price is None:
            continue
        price = price['content']

        # Extraer tamaño
        product_price = product.find('span', {'class': 'price'})
        if product_price is None:
            continue
        product_price = product_price.text.strip()
        tamanio = product_price.split('/')[1].strip() 
        
        
        
        # Extraer imagen
        image = product.find('img', {'itemprop': 'image'})
        if image is None:
            continue
        image = image['src']

        # Verificar si el producto ya ha sido agregado
        if (product_name, brand) in added_products:
            continue

        # Agregar el producto a la lista de productos agregados
        added_products.append((product_name, brand))

        # Obtener el número asignado a la marca
        marca_numero = brands.index(brand) + 1

        # Imprimir la información de cada producto
        print('Nombre del producto:', product_name)
        print('Marca:', brand)
        print('Precio:', price)
        print('Imagen:', image)
        print('Tamaño:', tamanio)
        print('---')

        # Insertar la información en la tabla de productos
        sql = "INSERT INTO productos (nombre, marca, precio, tamano, imagen, tipo, favorito) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (product_name, marca_numero, price, tamanio, image, 187, 0)
        cursor.execute(sql, val)
        db.commit()

    # Aumentar el número de página para navegar por la siguiente página
    page += 1

# Cerrar la conexión a la base de datos
db.close()

# Mensaje de finalización
print("Procesamiento de productos finalizado.")

#--------------------------------------------------------------------------------------------------------------