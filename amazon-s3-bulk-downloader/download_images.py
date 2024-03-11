import csv
import requests

# Ruta del archivo CSV
archivo_csv = "Solenopsis_Invicta-Solo-Enlaces.csv"

# Carpeta de destino
carpeta_destino = "./Data"

# Crea la carpeta de destino si no existe
import os
os.makedirs(carpeta_destino, exist_ok=True)

# Abre el archivo CSV
with open(archivo_csv, "r") as f:
  lector_csv = csv.reader(f)

  # Descarga cada foto
  for fila in lector_csv:
    url = fila[0]
    print(f"Procesando URL: {url}")  # Impresión de la URL

    # Obtiene el ID de la imagen de la URL
    id_imagen = url.split("/")[-2]

    # Descarga la foto
    print(f"Descargando {id_imagen}...")
    response = requests.get(url)
    with open(os.path.join(carpeta_destino, f"{id_imagen}.jpg"), "wb") as f:
      f.write(response.content)

print("Descarga completada.")
