import random

# crear gasto
def crear_gasto_operacional():
    num = random.randint(0, 12)
    if num >= 10:
        return 30000
    elif num < 10 and num >= 8:
        return 20000
    elif num < 8 and num >= 4:
        return 10000    
    else:
        return 0
