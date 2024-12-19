
import time
start_programu = time.time()

#Variana 1 importování
import math #když z jednoho modulu chceme importovat více funkcí
print(math.factorial(4))

#Variana 2 importování
from math import factorial #pokud je modul velký a chceme jenom jednu funkci
print(factorial(4))

#Variana 3 importování
import math as matika #pokud má modul lepší název nebo zkratku
print(matika.factorial(4))
#import numpy as np #IMPORT POUZE NA UKÁZKU!
#import pandas as pd

#Variana 4 importování
from math import * #nedoporučuji používat - nevíme odkud se funkce vzala
print(factorial(4))

import Example47funkce
Example47funkce.soucet_nasobek_podil(4,5)

import os
print(f"os.getlogin() {os.getlogin()}") #kdo je přihlášen k PC
print(os.getcwd()) #V jaké složce se nacházíme
print(os.listdir(r".")) #Získáme názvy všech souborů ve složce
print(os.path.isfile(r"C:\Users\alber\Desktop\4084\CZ4084\README.md"))
print(os.path.isfile("./reme.md"))
print(os.path.isfile("./README.md"))
#Zápis cesty: C:\Users\alber\Desktop\4084\CZ4084\README.md
#Zkráceně:                                     .\README.md
import sys
print(sys.argv)
print(sys.path)
import random
print(random.gauss(2))
time.sleep(2)
print(f"Program se vykonával: {time.time()-start_programu} sekund")

