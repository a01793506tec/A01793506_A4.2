# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qd0387-JKAWR7CMFq4_O9p1k7R0vFFYo
"""

import argparse
import time

#Funcion para cargar archivo
def procesar_archivo():
    """
     Funcion para cargar archivo
    """
    try:
        with open('FileWithData.txt', 'r', encoding='utf-8') as archivo_t:
            lineas = archivo_t.readlines()
            lineas_sin_nl = [linea.strip() for linea in lineas]
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except IOError:
        print("Error al abrir el archivo.")
    return lineas_sin_nl
#Funcion para validar dato numerico
def es_numerico(elemento_t):
    """    Funcion para validar si el elemento es numerico"""
    try:
        if int(elemento_t):
            return True
        if elemento_t == "0":
            return True
    except ValueError:
        return False
    return False

def decimal_a_binario(numero_t):
    """  Funcion para convertir numero a binario  """
    binariot = ''
    if numero_t == 0:
        return '0'

    while numero_t > 0:
        residuo = numero_t % 2
        binariot = str(residuo) + binariot
        numero_t = numero_t // 2
    return binariot

def a_hexadecimal(numero_t):
    """  Funcion para convertir numero a hexadecimal  """
    if numero_t == 0:
        return '0'

    hexadecimal = ''
    while numero_t > 0:
        residuo = numero_t % 16
        if residuo < 10:
            hexadecimal = str(residuo) + hexadecimal
        else:
            hexadecimal = chr(ord('A') + residuo - 10) + hexadecimal
        numero_t = numero_t // 16
    return hexadecimal

if __name__ == "__main__":
    inicio = time.time()
    with open('ConvertionResults.txt', 'w', encoding='utf-8') as archivo:
        parser = argparse.ArgumentParser(description='Procesar un archivo de texto.')
        parser.add_argument('archivo', help='Ruta del archivo de texto a procesar')
        args = parser.parse_args()

        lineas_sin_nueva_linea = procesar_archivo()

        numeros = []

        for elemento in lineas_sin_nueva_linea:
            VALOR_ELEMENTO = es_numerico(elemento)
            if VALOR_ELEMENTO:
                valor_absoluto = abs(int(elemento))
                numeros.append(valor_absoluto)
            else:
                print(f"{elemento} no es numérico")
                archivo.write(f"{elemento} no es numérico\n")

        numeros = [int(num) for num in numeros]
        TOTAL = 0

        for numero in numeros:
            BINARIO = decimal_a_binario(numero)
            hexa = a_hexadecimal(numero)
            archivo.write(f"El binario del elemento {numero} es:{BINARIO}\n")
            archivo.write(f"la base hexadecimal del elemento {numero} es:{hexa}\n")
            print("El binario del elemento", numero," es:", BINARIO)
            print("La base hexadecimal del elemento", numero," es:", hexa)
            TOTAL += 1
        print("El total de elementos es:", TOTAL)
        archivo.write(f"El total de elementos es:{TOTAL}\n")
        fin = time.time()
        tiempo_total = fin - inicio
        print("El tiempo de ejecución fue de:", tiempo_total, "segundos")
        archivo.write(f"El tiempo de ejecución fue de:{tiempo_total}")
