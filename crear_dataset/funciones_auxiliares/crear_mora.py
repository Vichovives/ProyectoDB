import random
import datetime

def crear_mora(monto, fecha_vencimiento, fecha_pago):
    fecha_pago_dt = datetime.datetime.strptime(fecha_pago, '%Y-%m-%d %H:%M:%S')
    fecha_vencimiento_dt = datetime.datetime.strptime(fecha_vencimiento, '%Y-%m-%d %H:%M:%S')
    dias_mora = fecha_pago_dt - fecha_vencimiento_dt
    if dias_mora.days == 0:
        return 0
    else:
        tasa_mora = 0.0001
        return round(monto * tasa_mora * dias_mora.days / 30)

