import numpy as np
import Funciones as fn

lista_rut = []
lista_entradas = []

def comprar_entradas():
    fn.cantidad_entradas()
    fn.fila()
    fn.columna()
    fn.validar_rut()


def ver_menu():
    while True:
        print("""Menu
        1.Comprar entradas
        2.Mostrar ubicaciones disponibles
        3.Ver listado de asistenetes 
        4.Mostrar ganancias totales
        5.Salir""")
        return

def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opcion: "))
            if opcion in (1,2,3,4,5):
                return opcion
            else:
                print("ERROR! Opcion incorrecta")
        except:
            print("ERROR! Ingrese un numero entero")


def cantidad_entradas():
    while True:
        try:
            entradas = int(input("Ingrese cantidad de entradas: "))
            if entradas <=3:
                return entradas
            else:
                print("ERROR! Cantidad de entradas incorrecta")
        except:
            print("ERROR! Ingrese un numero entero")


def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut: "))
            if len(str(rut)) >= 7 and len(str(rut)) <= 8:
                return rut
            else:
                print("ERROR! Rut incorrecto")
        except:
            print("ERROR! Ingrese numero entero")

def fila():
    while True:
        try:
            fila = int(input("Ingrese fila: "))
            if fila <= 10:
                return fila
            else:
                print("ERROR! Fila incorrecta")
        except:
            print("ERROR! Ingrese un numero entero")

def columna():
    while True:
        try:
            columna = int(input("Ingrese columna: "))
            if columna <= 100:
                return columna
            else:
                print("ERROR! columna incorrecta")
        except:
            print("ERROR! Ingrese un numero entero")

def asistentes():
    if lista_rut in []:
        return lista_rut

        
def ganancias():
    fn.cantidad_entradas 
    print("""|Tipo de entrada | Cantidad | Total |
             |________________|__________|_______|
             |________________|__________|_______|
             |Total           |__________|_______|""") 


def salir():
    print("Samuel Cortez 11-07-2023")