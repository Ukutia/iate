from datetime import datetime
import datetime
from iate.code import dayname
import random
import time


def evaluar(arc):
    archivo = open(arc, "r")
    lista = []
    for linea in archivo:
        l = linea.strip().split()
        lista.append(l)
    a = []
    for b in lista:
        x = b[0]
        y = b[4]
        z = [x, y]
        a.append(z)
        #agregar base de datos resultante
    i = 0
    status = []
    x = random.randint(0, len(a) - 1)
    b = a[x]
    c = b[1]
    if int(c) > 0 and x % 2 == 0:
        c = int(c) - 1
        a[x].insert(1, c)
        del a[x][2]
        status.append("Hay fila")
    else:
        status.append("No hay fila")
    i = i+1
    return(status[-1])