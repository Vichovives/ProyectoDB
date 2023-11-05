import random
import datetime

def crear_fecha_pago(fecha_curse, fecha_vencimiento):
    fecha_vencimiento_dt = datetime.datetime.strptime(fecha_vencimiento, '%Y-%m-%d %H:%M:%S')
    fecha_curse_dt = datetime.datetime.strptime(fecha_curse, '%Y-%m-%d %H:%M:%S')

    en_plazo = random.randint(0,4) #se paga en plazo o no
    if (en_plazo == 0):
        dias_atraso = random.randint(1,60)
        fecha_pago = fecha_vencimiento_dt + datetime.timedelta(days=dias_atraso)
        return fecha_pago.strftime('%Y-%m-%d %H:%M:%S')
    else:
        return fecha_vencimiento