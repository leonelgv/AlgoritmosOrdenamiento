import random
from time import time
from aBurbuja import Burbuja

a = []
b = Burbuja()


for i in range(0, 1000):
    a.append(random.randint(0,10000))

print (a)

inicio = time()
c = b.bubbleSort(a)
t_final = time() - inicio
print (c)
print (t_final)

