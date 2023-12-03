import random

def crear_porcentaje_anticipo():
    num = random.randint(1,10)
    if num == 1:
        return 1 - 0
    elif num > 1 and num <= 4:
        return 1 - 0.05
    elif num > 4 and num <= 8:
        return 1 - 0.1
    else:
        return 1 - 0.15