import random
import datetime

def crear_numero_dias(fecha_actual, fecha_vencimiento):
    fecha_vencimiento_dt = datetime.datetime.strptime(fecha_vencimiento, '%Y-%m-%d %H:%M:%S')
    dias = fecha_actual - fecha_vencimiento_dt
    return dias.days
    