import sys
from PIL import Image
import os

# Obtiene el directorio de la carpeta desde la línea de comandos
if len(sys.argv) < 2:
    print("Debe proporcionar el directorio de la carpeta como argumento.")
    sys.exit()
ruta_carpeta = sys.argv[1]

# Lista todos los archivos de la carpeta
archivos = os.listdir(ruta_carpeta)

# Verifica si hay exactamente tres imágenes en la carpeta
imagenes = [archivo for archivo in archivos if os.path.isfile(os.path.join(ruta_carpeta, archivo)) and archivo.lower().endswith((".png", ".jpg", ".jpeg"))]
if len(imagenes) != 3:
    raise Exception(f"La carpeta debe contener exactamente tres imágenes, se encontraron {len(imagenes)} imágenes.")
else:
    # Recorre todos los archivos de la carpeta
    for archivo in archivos:
        # Obtiene la ruta completa del archivo
        ruta_archivo = os.path.join(ruta_carpeta, archivo)

        # Verifica si el archivo es una imagen
        if os.path.isfile(ruta_archivo) and archivo.lower().endswith((".png", ".jpg", ".jpeg")):
            # Carga la imagen y verifica si ya está en monocromático
            imagen = Image.open(ruta_archivo)
            if imagen.mode == "L":
                print(f"La imagen {archivo} ya está en monocromático.")
                continue

            # Convierte la imagen a monocromático
            imagen_monocromo = imagen.convert("L")

            # Guarda la imagen monocromática con el mismo nombre y extensión que el archivo original
            ruta_archivo_monocromo = os.path.join(ruta_carpeta, archivo)
            imagen_monocromo.save(ruta_archivo_monocromo)

            # Cierra la imagen original y la imagen monocromática
            imagen.close()
            imagen_monocromo.close()
