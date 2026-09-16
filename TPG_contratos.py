# FUNCIONES DE PRODUCTOS

def registrar_producto(productos: dict) -> dict:
    """
    Permite registrar un producto nuevo al programa.
    Pre: Recibe el diccionario con los datos de los productos.
    Post: Devuelve el diccionario actualizado con los datos del nuevo producto.
    """



def eliminar_producto(productos: dict) -> dict:
    """
    Permite eliminar un producto en base a su nombre o id.
    Pre: Recibe el diccionario que contiene todos los datos de todos los productos.
    Post: Devuelve el diccionario actualizado sin los datos del producto que fue eliminado.
    """



def buscar_producto(productos: dict) -> str:
    """
    Permite buscar un producto por su nombre o id.
    Pre: Recibe el diccionario que contiene los nombres y los id's.
    Post: Retorna un string con los datos del producto que se queria buscar.
    """



def modificar_stock(productos: dict) -> dict:
    """
    Permite modificar el stock de un producto.
    Pre: recibe el diccionario con los datos de todos los productos.
    Post: devuelve el diccionario actualizado con el stock modificado.
    """



def modificar_precio(dict: dict) -> dict:
    """
    Permite modificar el precio de un producto.
    Pre: Recibe el diccionario con los datos de todos los productos.
    Post: Devuelve el diccionario con el precio actualizado.
    """



# FUNCIONES DE VENTAS



# FUNCIONES DE CONSULTA / MENÚ 

def imprimir_productos(productos: dict )-> None:
    """
    Recorre e imprime la informacion de cada producto almacenado en el diccionario 
    
    pre: Recibe un diccionario con toda la informacion de los productos

    Post:Imprime en consola los datos de todos los  productos.
  """      

def ordenar_productos(productos:dict)-> None:
    """
    Ordena los productos por orden alfabetico 
    pre: Recibe el diccionario con todos los productos 
    post: Muestra en pantalla todos los productos ordenados 
    """

def total_facturado(ventas:dict)-> int:

    """
    Imprime la suma total de todas las ventas 
    pre: Recibe el diccionario con todos los datos de las ventas
    post: Retorna la suma de todas las ventas como un número entero 

    """

def prod_mas_vendido(productos:dict)-> None:
    """
    Muestra en pantalla el producto más vendido
    pre: Recibe el diccionario de ventas 
    post: no retorna nada, solo imprime el producto con mayor ventas
    """

def mostrar_menu() -> None:
    """
    Imprime las opciones disponibles en la consola
    
    pre:No recibe nada 
    post: No retorna nada, solo muestra las opciones al usuario.
    """
def main()-> None:
    """
    Ejecuta el código principal
    pre:No recibe nada
    post:No retorna nada, permite usar el código
    """