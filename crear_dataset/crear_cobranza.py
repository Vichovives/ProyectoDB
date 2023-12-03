import csv
import random
import string
import datetime
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
from funciones_auxiliares import crear_porcentaje_anticipo as cpa
from funciones_auxiliares import crear_numero_dias as cnd

# Nos conectamos a la db
conn = initializers.DBInstance()
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# Se crea la tabla
columns_cobranza = [
    "cobranza_deudor varchar(120) not null",
    "cobranza_numero_operacion integer not null",
    "cobranza_fecha_curse timestamp not null",
    "cobranza_numero_dcto integer primary key not null unique",
    "cobranza_fecha_emision timestamp not null",
    "cobranza_vencimiento_original timestamp not null",
    "cobranza_vencimiento timestamp not null",
    "cobranza_estado_dcto varchar(40) not null",
    "cobranza_numero_dias smallint not null",
    "cobranza_valor_dcto bigint not null",
    "cobranza_valor_anticipo bigint not null",
    "cobranza_saldo_dcto bigint not null",
    "cobranza_estado_cobranza varchar(40) default 'Dcto Nuevo'",
    "cobranza_proximo_llamado timestamp",
    "cobranza_fecha_pago timestamp",
    "cobranza_ultima_gestion timestamp"
]

columns_evento = [
    "cobranza_evento_dcto integer references cobranzas(cobranza_numero_dcto)",
    "cobranza_evento_estado varchar(30) not null",
    "cobranza_evento_fecha_pago timestamp",
    "cobranza_evento_observacion varchar(200)"
]

create_table.create_table(cursor, "cobranzas", columns_cobranza)
create_table.create_table(cursor, "cobranza_eventos", columns_evento)

ROWS = 10

empresas = []
with open('empresas.csv', mode='r', newline='', encoding='utf-8') as empresas_file:
    reader = csv.reader(empresas_file, delimiter=';')
    for row in reader:
        empresas.append(row)

empresas_lista = []
for i in range (ROWS):
    empresa_random = random.choice(empresas)
    empresas_lista.append(empresa_random)

for i in range(ROWS):
    valor_dcto = random.randint(40000,1000000)
    fecha_curse = cfc.crear_fecha_curse(datetime.datetime(2023,8,5), datetime.datetime(2023,11,5))
    valor_dcto = random.randint(40000,1000000)
    fecha_vencimiento = fecha_vencimiento = cfv.crear_fecha_vencimiento(fecha_curse)
    porcenteja_anticipo = cpa.crear_porcentaje_anticipo()
    fecha_actual = datetime.datetime(2023,11,5)
    cobranza = {
        "cobranza_deudor": empresas_lista[i][2],
        "cobranza_numero_operacion": (i+1)*8,
        "cobranza_fecha_curse": fecha_curse,
        "cobranza_numero_dcto": i,
        "cobranza_fecha_emision": fecha_vencimiento,
        "cobranza_vencimiento_original": fecha_vencimiento,
        "cobranza_vencimiento": fecha_vencimiento,
        "cobranza_estado_dcto": "Aceptada" if random.random() <= 0.8 else "Rechazada",
        "cobranza_numero_dias": cnd.crear_numero_dias(datetime.datetime(2023, 11, 6), fecha_vencimiento),
        "cobranza_valor_dcto": valor_dcto,
        "cobranza_valor_anticipo": valor_dcto*porcenteja_anticipo,
        "cobranza_saldo_dcto": valor_dcto,
        "cobranza_estado_cobranza": "Gestionado",
        "cobranza_proximo_llamado": fecha_vencimiento,
        "cobranza_ultima_gestion": fecha_actual.strftime('%Y-%m-%d %H:%M:%S')
    }

    insert_into.insert_into(cursor, "cobranzas", cobranza)
    print(f"Registro {i} creado")
    for j in range(3):
        cobranza_evento = {
            "cobranza_evento_dcto": i,
            "cobranza_evento_estado": "Gestionado",
            "cobranza_evento_observacion": "Se gestiono, aun no hay fecha de pago"
        }
        insert_into.insert_into(cursor, "cobranza_eventos", cobranza_evento)
        print(f"Registro {i} -> {j} creado")


cursor.close()
conn.close()