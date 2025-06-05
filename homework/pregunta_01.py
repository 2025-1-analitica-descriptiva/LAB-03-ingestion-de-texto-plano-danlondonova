"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import re

def pregunta_01(filepath='files/input/clusters_report.txt'):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    lines = [line.rstrip() for line in lines]
    lines = lines[4:]  # quitar encabezados

    data = []
    buffer = ""
    for line in lines:
        if re.match(r"\s*\d+\s+", line):  # nueva fila detectada
            if buffer:
                data.append(buffer)
            buffer = line
        else:
            buffer += ' ' + line
    if buffer:
        data.append(buffer)

    parsed = []
    for row in data:
        parts = re.split(r'\s{2,}', row.strip())
        if len(parts) >= 4:
            cluster = int(parts[0])
            cantidad = int(parts[1])
            porcentaje = float(parts[2].replace(',', '.').replace('%', ''))
            palabras = parts[3:]
            palabras = ' '.join(palabras).replace('.', '')
            palabras = re.sub(r'\s+', ' ', palabras).strip()
            parsed.append([cluster, cantidad, porcentaje, palabras])

    df = pd.DataFrame(parsed, columns=[
        'cluster',
        'cantidad_de_palabras_clave',
        'porcentaje_de_palabras_clave',
        'principales_palabras_clave'
    ])
    return df


"""
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
