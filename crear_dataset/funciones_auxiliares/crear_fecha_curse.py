import random
import datetime

def crear_fecha_curse(start_date = datetime.datetime(2020,1,1), end_date = datetime.datetime(2023,12,31)):

    random_datetime = start_date + (end_date - start_date) * random.random()
    timestamp_string = random_datetime.strftime('%Y-%m-%d %H:%M:%S')
    return timestamp_string

