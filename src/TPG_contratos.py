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
