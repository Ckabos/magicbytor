#!/usr/bin/python3

# -----------------------------------------------------------------------------
#                               Magicbytor
#                             by Ckabos
# -----------------------------------------------------------------------------

import argparse
from datetime import datetime
import os

def generar_archivo(tipo_archivo, contenido, nombre_archivo=None):
    """
    Función que genera un archivo binario con el tipo de archivo especificado
    y los correspondientes "magic bytes". Agrega el contenido proporcionado
    por el usuario al archivo generado.

    Args:
    - tipo_archivo (str): Tipo de archivo (jpg, png, pdf, etc.).
    - contenido (str): Contenido adicional a incluir en el archivo.
    - nombre_archivo (str, opcional): Nombre del archivo generado. Si no se proporciona,
                                      se genera un nombre con timestamp.

    Returns:
    - None
    """

    # Lista de "magic bytes" para diferentes tipos de archivo
    magic_bytes = {
        'jpg': [0xFF, 0xD8, 0xFF, 0xE0],
        'png': [0x89, 0x50, 0x4E, 0x47],
        'pdf': [0x25, 0x50, 0x44, 0x46, 0x2D, 0x31, 0x2E, 0x30],  # Magic bytes de PDF (%PDF-1.x)
        'gif': [0x47, 0x49, 0x46, 0x38, 0x39, 0x61],  # GIF
        'mp3': [0x49, 0x44, 0x33],
        'avi': [0x52, 0x49, 0x46, 0x46],  # AVI
        'xml': [0x3C, 0x3F, 0x78, 0x6D, 0x6C, 0x20],  # XML
        'mp4': [0x00, 0x00, 0x00, 0x18, 0x66, 0x74, 0x79, 0x70],  # MP4
    }

    # Verificar si el tipo de archivo está en los "magic bytes" soportados
    if tipo_archivo not in magic_bytes:
        print(f"Tipo de archivo '{tipo_archivo}' no soportado.")
        return

    magic = magic_bytes[tipo_archivo]

    # Para JSON, agregar la apertura con '{' o '[' para que sea un JSON válido
    if tipo_archivo == 'json':
        contenido_json = f'{{"data": "{contenido}"}}'  # Aseguramos que sea un JSON válido
    else:
        contenido_json = contenido  # Para otros archivos solo añadir contenido

    # Crear el contenido final con magic bytes y lo que se pasa por argumento
    archivo_contenido = bytearray(magic)
    archivo_contenido.extend(contenido_json.encode('utf-8'))

    # Si no se proporciona un nombre de archivo, usar un timestamp para asegurar un nombre único
    if not nombre_archivo:
        nombre_archivo = f"archivo_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    # Verificar si el nombre de archivo tiene una extensión
    if '.' in nombre_archivo:
        # Si tiene una extensión, no agregar la extensión del tipo de archivo
        filename = nombre_archivo
    else:
        # Si no tiene extensión, agregar la extensión del tipo de archivo
        filename = f"{nombre_archivo}.{tipo_archivo}"

    # Guardar el archivo en el directorio actual
    with open(filename, "wb") as f:
        f.write(archivo_contenido)

    print(f"Archivo '{filename}' generado con éxito.")

def main():
    """
    Función principal que procesa los argumentos de línea de comandos y
    llama a la función `generar_archivo` con los parámetros adecuados.

    Args:
    - None

    Returns:
    - None
    """

    # Crear el parser de argumentos
    parser = argparse.ArgumentParser(description="Generador de archivos con magic bytes.")

    # Definir los argumentos que se aceptarán en la línea de comandos
    parser.add_argument("-c", "--contenido", required=True, help="Contenido adicional a agregar al archivo.")
    parser.add_argument("-n", "--name", help="Nombre personalizado para el archivo generado (opcional).", default=None)
    parser.add_argument("-b", "--bytes", help="Tipo de magic bytes a usar para el archivo (predefinido por tipo de archivo).",
                        choices=['jpg', 'png', 'pdf', 'gif', 'zip', 'mp3', 'txt', 'bmp', 'exe', 'avi', 'tar', 'html', 'csv', 'xml', 'json', 'mp4', 'docx', 'xlsx'], required=True)

    # Parsear los argumentos
    args = parser.parse_args()

    # Usar el tipo de archivo que viene con -b para la función
    generar_archivo(args.bytes, args.contenido, args.name)

if __name__ == "__main__":
    main()

