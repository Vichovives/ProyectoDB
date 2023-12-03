import random

def crear_gasto_administrativo(x):
    factor = x * random.randint(0,5) #min=0 max=60
    if factor == 5:
        return x*10000
    if factor == 4:
        num = round(x/2)
        return num*10000
    else:
        return 0