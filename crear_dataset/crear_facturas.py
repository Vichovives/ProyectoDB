import csv
import random
from datetime import datetime


# de las empresas sacamos una linea random y conseguimos los datos
empresas = []
with open('empresas.csv', mode='r', newline='', encoding='utf-8') as empresas_file:
    reader = csv.reader(empresas_file, delimiter=';')
    for row in reader:
        empresas.append(row)




# Generamos las facturas ficticias

# puse 10000, porque esas son las tuplas, podemos cambiarla segun lo que ncesitemos
# rango de fecha de las facturas
start_date = datetime(2020, 1, 1)
end_date = datetime(2023, 11, 3)

facturas = []
for i in range(10000):
    empresa = random.choice(empresas)
    fecha_emision = start_date + (end_date - start_date) * random.random()
    fecha_emision_str = fecha_emision.strftime('%Y-%m-%d %H:%M:%S')  # Formatear la fecha sin milisegundos
    factura = {
        "folio": i + 1,
        "rut_deudor": empresa[1],
        "razon_social_deudor": empresa[2],
        "monto": random.randint(1,9999999999999),
        "fecha_emision": fecha_emision_str,
        "estado_ssi": "Aceptada" if random.random() <= 0.8 else "Rechazada"
    }

    facturas.append(factura)



# Escribir el archivo csv
# Puede que no sea necesario escribirlo en csv, podriamos desde aqui insertar a la base de datos, pero puede ayudar a mantener consistencia con los datos

with open("lista_facturas.csv", mode="w", newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=facturas[0].keys())
    writer.writeheader()
    writer.writerows(facturas)