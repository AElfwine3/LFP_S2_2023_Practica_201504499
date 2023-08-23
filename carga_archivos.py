import tkinter as tk
from tkinter import filedialog
from tabulate import tabulate
import os

productos = []

def agregar_stock(nombre, cantidad, bodega):
    for producto in productos:
        if producto['nombre'] == nombre:
            if producto['bodega'] == bodega:
                producto['cantidad'] += cantidad
                return
            else:
                print(f'El producto {producto["nombre"]} no existe en bodega {producto["bodega"]}')
                return

def vender_producto(nombre, cantidad, bodega):
    for producto in productos:
        if producto['nombre'] == nombre:
            if producto['bodega'] == bodega:
                if producto['cantidad'] < cantidad:
                    print(f'No hay suficiente stock de {nombre} en {bodega}')
                    return
                else:
                    producto['cantidad'] -= cantidad
                    return

def carga_inventario():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()

    if not file_path.endswith('.inv'):
        print('No es un archivo valido')
    else:
        with open(file_path, 'r') as file:
            for line in file:
                datos = [dato.strip() for dato in line.rstrip().split(';')]
                producto = {
                    'nombre': datos[0].split()[1],
                    'cantidad': int(datos[1]),
                    'precio': datos[2],
                    'bodega': datos[3]
                }
                if datos[0].split()[0] == 'crear_producto':
                    productos.append(producto)
    print('Inventario cargado con exito!!!')


def carga_movimientos():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()

    if not file_path.endswith('.mov'):
        print('No es un archivo valido')
    else:
        with open(file_path, 'r') as file:
            for line in file:
                datos = [dato.strip() for dato in line.rstrip().split(';')]
                movimiento = {
                    'nombre': datos[0].split()[1],
                    'cantidad': int(datos[1]),
                    'bodega': datos[2]
                }
                if datos[0].split()[0] == 'agregar_stock':
                    agregar_stock(movimiento['nombre'], movimiento['cantidad'], movimiento['bodega'])
                elif datos[0].split()[0] == 'vender_producto':
                    vender_producto(movimiento['nombre'], movimiento['cantidad'], movimiento['bodega'])
    print('Movimientos realizados con exito!!!')

def reporte_inventario():
    tabla = [
        [producto['nombre'], producto['cantidad'], producto['precio'], producto['cantidad'] * float(producto['precio']), producto['bodega']]
        for producto in productos
    ]
    
    with open('reporte.txt', 'w') as file:
        file.write(tabulate(tabla, headers=['Producto', 'Cantidad', 'Precio Unitario', 'Valor Total', 'Ubicacion']))
    
    os.system('start reporte.txt')
