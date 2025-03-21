# Generador de Archivos con Magic Bytes

Este proyecto permite generar archivos con **magic bytes** específicos de varios tipos de archivo, lo que es útil para pruebas de seguridad, simulaciones de archivos maliciosos, y otros fines técnicos.

## Descripción

El script **magicbytor.py** genera archivos con magic bytes que corresponden a diferentes tipos de archivos como imágenes (JPG, PNG), documentos (PDF, Word), archivos de audio (MP3), entre otros. También permite agregar contenido personalizado a los archivos generados.

**Magic bytes** son secuencias específicas de bytes al principio de un archivo que identifican su tipo. El script permite simular varios tipos de archivos utilizando estos magic bytes.

## Requisitos

- Python 3.x
- No requiere librerías adicionales fuera de las bibliotecas estándar de Python.

## Uso

1. **Clona el repositorio o descarga el archivo `magicbytor.py`.**

2. **Ejecuta el script con los siguientes parámetros:**
   ```bash
   python3 magicbytor.py -c "<contenido>" -n "<nombre_del_archivo>" -b <tipo_de_archivo>

## Parámetros:

`-c` o `--contenido`: Contenido adicional que deseas incluir en el archivo generado. Este parámetro es obligatorio.

`-n` o `--name`: Nombre personalizado para el archivo generado (opcional). Si no se proporciona, se usará un nombre basado en la fecha y hora actuales.

`-b` o `--bytes`: Tipo de archivo que deseas generar. Este parámetro es obligatorio y debes especificar uno de los siguientes tipos:

- jpg
- png
- pdf
- gif
- mp3
- avi
- xml
- mp4

## Ejemplos de uso:

Generar un archivo PDF con contenido personalizado (por ejemplo, código PHP):

```bash
python3 magicbytor.py -c "<?php echo 'Hola Mundo'; ?>" -n custom_file.php -b jpg
```
Esto generará un archivo custom_file.php con el contenido PHP especificado.

Generar un archivo MP3 con texto:

```bash
python3 magicbytor.py -c "Este es un archivo de prueba" -n prueba.php -b mp3
```
Esto generará un archivo prueba.mp3 con el texto dentro.

Generar un archivo XML con contenido personalizado:

```bash
python3 magicbytor.py -c "<data>Sample</data>" -n archivo.xml -b xml
```

Esto generará un archivo archivo.xml con el contenido XML proporcionado.

## Notas:
Si no proporcionas un nombre para el archivo, el script usará un nombre basado en la fecha y hora actuales, como archivo_20230320_142512.

El tipo de archivo se selecciona mediante el parámetro -b y los magic bytes correspondientes se agregarán al archivo.

El contenido del archivo será añadido después de los magic bytes.
