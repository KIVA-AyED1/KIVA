# FUNCIONES DE PRODUCTOS

def registrar_producto(productos: dict) -> dict:
    """
    Permite registrar un producto nuevo al programa.
    Pre: Recibe el diccionario con los datos de los productos.
    Post: Devuelve el diccionario actualizado con los datos del nuevo producto.
    """
    print("Función registrar producto: Permite registrar un producto.")



def eliminar_producto(productos: dict) -> dict:
    """
    Permite eliminar un producto en base a su nombre o id.
    Pre: Recibe el diccionario que contiene todos los datos de todos los productos.
    Post: Devuelve el diccionario actualizado sin los datos del producto que fue eliminado.
    """
    print("Funcion eliminar_producto: Peermite eliminar un producto del programa.")



def buscar_producto(productos: dict) -> str:
    """
    Permite buscar un producto por su nombre o id.
    Pre: Recibe el diccionario que contiene los nombres y los id's.
    Post: Retorna un string con los datos del producto que se queria buscar.
    """
    print("Funcion buscar_producto: Permite buscar un producto y ver todos sus datos (id, nombre, precio y stock).")



def modificar_stock(productos: dict) -> dict:
    """
    Permite modificar el stock de un producto.
    Pre: recibe el diccionario con los datos de todos los productos.
    Post: devuelve el diccionario actualizado con el stock modificado.
    """
    print("Funcion modificar_stock: Permite modificar el stock de un producto.")



def modificar_precio(dict: dict) -> dict:
    """
    Permite modificar el precio de un producto.
    Pre: Recibe el diccionario con los datos de todos los productos.
    Post: Devuelve el diccionario con el precio actualizado.
    """
    print("Funcion modificar_precio: Permite modificar el precio de un producto.")



# FUNCIONES DE VENTAS


def registrar_venta(ventas: dict, productos: dict) -> dict:
    """
    Registra una nueva venta y descuenta el stock del producto vendido.
    
    Pre: Recibe el diccionario de ventas y el diccionario de productos.
    Post: Devuelve el diccionario de ventas actualizado con la nueva venta registrada.
    """
    print("Función registrar_venta: Registra una nueva venta y actualiza el stock.")


def eliminar_venta(ventas: dict) -> dict:
    """
    Elimina un registro de venta en base a su ID.
    
    Pre: Recibe el diccionario con todos los datos de las ventas.
    Post: Devuelve el diccionario de ventas actualizado sin la venta eliminada.
    """
    print("Función eliminar_venta: Elimina una venta seleccionada.")


def modificar_venta(ventas: dict, productos: dict) -> dict:
    """
    Modifica la cantidad de una venta realizada y reajusta el stock.
    
    Pre: Recibe el diccionario de ventas y el diccionario de productos.
    Post: Devuelve el diccionario de ventas con la cantidad y el total actualizados.
    """
    print("Función modificar_venta: Modifica una venta y ajusta el stock.")


def mostrar_ventas(ventas: dict) -> None:
    """
    Muestra en pantalla el listado de todas las ventas registradas.
    
    Pre: Recibe el diccionario con todos los datos de las ventas.
    Post: No retorna nada, solo imprime en consola la información de las ventas.
    """
    print("Función mostrar_ventas: Imprime el historial de ventas.")


def calcular_vuelto(total: float, monto_pagado: float) -> float:
    """
    Calcula el vuelto que se le debe entregar al cliente.
    
    Pre: Recibe el monto total a pagar y el dinero entregado por el cliente.
    Post: Retorna el monto a devolver como un número decimal (float).
    """
    print("Función calcular_vuelto: Calcula la diferencia a devolver.")
    

# FUNCIONES DE CONSULTA / MENÚ 

def imprimir_productos(productos: dict )-> None:
    """
    Recorre e imprime la informacion de cada producto almacenado en el diccionario 
    
    pre: Recibe un diccionario con toda la informacion de los productos

    Post:Imprime en consola los datos de todos los  productos.
  """      
    print("funcion imprimir_productos: Muestra todos los productos almacenados")

def ordenar_productos(productos:dict)-> None:
    """
    Ordena los productos por orden alfabetico 
    pre: Recibe el diccionario con todos los productos 
    post: Muestra en pantalla todos los productos ordenados 
    """
    print("funcion ordenar_productos: muestra los productos en orden alfabetico")

def total_facturado(ventas:dict)-> int:

    """
    Imprime la suma total de todas las ventas 
    pre: Recibe el diccionario con todos los datos de las ventas
    post: Retorna la suma de todas las ventas como un número entero 

    """
    print("funcion total_facturado: Muestra el total de las ventas")

def prod_mas_vendido(productos:dict)-> None:
    """
    Muestra en pantalla el producto más vendido
    pre: Recibe el diccionario de ventas 
    post: no retorna nada, solo imprime el producto con mayor ventas
    """
    print("Funcion prod_mas_vendido: Muestra el producto más vendido")

def mostrar_menu() -> None:
    """
    Imprime las opciones disponibles en la consola
    
    pre:No recibe nada 
    post: No retorna nada, solo muestra las opciones al usuario.
    """

    print("KIVA\n\n")
    print("Elija una opcion\n")
    print("1. Cargar un nuevo producto.")
    print("2. Eliminar un producto.")
    print("3. Buscar un producto.")
    print("4. Modificar el stock de un producto")
    print("5. Modificar el precio de un producto.")
    print("6. Registrar venta.")
    print("7. Eliminar venta.")
    print("8. Modificar venta del dia.")
    print("9. Mostrar ventas.")
    print("10. Calcular el vuelto de una venta.")
    print("11. Mostrar lista de productos.")
    print("12. Elegir orden de los productos.")
    print("13. Mostrar total facturado.")
    print("14. Revisar el producto mas vendido.")
    print("15. Pasar al dia siguiente.")
    

def main()-> None:
    """
    Ejecuta el código principal
    pre:No recibe nada
    post:No retorna nada, permite usar el código
    """
    productos = {"nombres": [], "ids": [], "precios": [], "stock": []}
    ventas = {"dias": [], "ganancias": [], "cantidad": []}
    dia = 1
    total = 0
    monto = 0
    venta_de_hoy = (0, 0)
    while True:
        mostrar_menu()
        print()
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            registrar_producto(productos)
        elif opcion == "2":
            eliminar_producto(productos)
        elif opcion == "3":
            buscar_producto(productos)
        elif opcion == "4":
            modificar_stock(productos)
        elif opcion == "5":
            modificar_precio(productos)
        elif opcion == "6":
            registrar_venta(ventas, productos)
        elif opcion == "7":
            eliminar_venta(ventas)
        elif opcion == "8":
            modificar_venta(ventas, productos)
        elif opcion == "9":
            mostrar_ventas(ventas)
        elif opcion == "10":
            calcular_vuelto(total, monto)
        elif opcion == "11":
            imprimir_productos(productos)
        elif opcion == "12":
            ordenar_productos(productos)
        elif opcion == "13":
            total_facturado(ventas)
        elif opcion == "14":
            prod_mas_vendido(productos)
        elif opcion == "15":
            dia += 1
            print("Pasa de día y carga las ventas. ")
        else:
            print("Opción Inválida. ")


main()

    