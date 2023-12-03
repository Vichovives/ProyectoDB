import random
import datetime

def crear_fecha_vencimiento(fecha_curse):
    fecha_curse_dt = datetime.datetime.strptime(fecha_curse, '%Y-%m-%d %H:%M:%S')
    plazo = random.randint(1,5)
    if plazo == 1 or plazo == 2:
        fecha_vencimiento = fecha_curse_dt + datetime.timedelta(days=30)
        return fecha_vencimiento.strftime('%Y-%m-%d %H:%M:%S')
    elif plazo == 3 or plazo == 4:
        fecha_vencimiento = fecha_curse_dt + datetime.timedelta(days=60)
        return fecha_vencimiento.strftime('%Y-%m-%d %H:%M:%S')
    else:
        fecha_vencimiento = fecha_curse_dt + datetime.timedelta(days=90)
        return fecha_vencimiento.strftime('%Y-%m-%d %H:%M:%S')


    