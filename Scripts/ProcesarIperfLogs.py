#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:53:58 2026

@author: lex
"""

import os
import re

def procesar_archivo(ruta_txt):
    with open(ruta_txt, 'r', encoding='utf-8') as f:
        lineas = f.readlines()

    # 1–3. Eliminar primeras 3 líneas y últimas 8 líneas
    lineas = lineas[3:-8]

    if not lineas:
        return

    # 4. Mantener encabezado intacto
    encabezado = lineas[0].strip()
    datos = lineas[1:]

    # 5. Separar líneas pares (TX-C) e impares (RX-C)
    # (según condición dada, no por índice)
    lineas_tx = [l.strip() for l in datos if "TX-C" in l]
    lineas_rx = [l.strip() for l in datos if "RX-C" in l]

    # Reorganizar: primero TX-C, luego RX-C
    datos_ordenados = lineas_tx + lineas_rx

    # 6. Reemplazar espacios (1 a 5) por coma
    def limpiar(linea):
        return re.sub(r' {1,5}', ',', linea)

    encabezado_csv = limpiar(encabezado)
    datos_csv = [limpiar(l) for l in datos_ordenados]

    # 7. Guardar como CSV
    ruta_csv = os.path.splitext(ruta_txt)[0] + ".csv"
    with open(ruta_csv, 'w', encoding='utf-8') as f:
        f.write(encabezado_csv + "\n")
        for linea in datos_csv:
            f.write(linea + "\n")

    print(f"Procesado: {ruta_txt} -> {ruta_csv}")


def procesar_carpeta(carpeta):
    for archivo in os.listdir(carpeta):
        if archivo.lower().endswith(".txt"):
            ruta_completa = os.path.join(carpeta, archivo)
            procesar_archivo(ruta_completa)


if __name__ == "__main__":
    carpeta = "./"  # Cambia esto por la ruta deseada
    procesar_carpeta(carpeta)