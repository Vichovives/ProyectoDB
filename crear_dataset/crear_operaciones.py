import csv
import random
import string

import psycopg2
import psycopg2.extras

from database import initializers

from queries import create_table
from queries import insert_into

from funciones_auxiliares import crear_gasto_administrativo as cga
from funciones_auxiliares import crear_gasto_operacion as cgo
from funciones_auxiliares import crear_fecha_curse as cfc
from funciones_auxiliares import crear_fecha_vencimiento as cfv
from funciones_auxiliares import crear_fecha_pago as cfp
from funciones_auxiliares import crear_mora as cm

# Nos conectamos a la db
conn = initializers.DBInstance()
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# Se crea la tabla

columns = [
    "operacion_cliente bigint primary key NOT NULL unique",
    "operacion_cantidad_facturas smallint NOT NULL",
    "operacion_gasto_operacional bigint NOT NULL",
    "operacion_gasto_administrativo bigint NOT NULL",
    "operacion_monto bigint NOT NULL",
    "operacion_interes real NOT NULL",
    "operacion_mora bigint NOT NULL",
    "operacion_fecha_curse timestamp NOT NULL",
    "operacion_fecha_vencimiento timestamp NOT NULL",
    "operacion_fecha_pago timestamp NOT NULL"
]

create_table.create_table(cursor, "operacions", columns)


for i in range(10000):
    cantidad_facturas = random.randint(1,12)
    monto = random.randint(40000,1000000)
    fecha_curse = cfc.crear_fecha_curse()
    fecha_vencimiento = cfv.crear_fecha_vencimiento(fecha_curse)
    fecha_pago = cfp.crear_fecha_pago(fecha_curse, fecha_vencimiento)
    operacion = {
        "operacion_cliente": i,
        "operacion_cantidad_facturas": cantidad_facturas,
        "operacion_gasto_operacional": cgo.crear_gasto_operacional(),
        "operacion_gasto_administrativo": cga.crear_gasto_administrativo(cantidad_facturas),
        "operacion_monto": monto,
        "operacion_interes": round(random.uniform(0.03, 0.009), 6),
        "operacion_mora": cm.crear_mora(monto, fecha_vencimiento, fecha_pago),
        "operacion_fecha_curse": fecha_curse,
        "operacion_fecha_vencimiento": fecha_vencimiento,
        "operacion_fecha_pago": fecha_pago
    }
    insert_into.insert_into(cursor, "operacions", operacion)
    print(f"Registro {i} creado")
    
cursor.close()
conn.close()

"""
with open("lista_operaciones.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=operaciones_lista[0].keys())
    writer.writeheader()
    writer.writerows(operaciones_lista)
"""
