#!/usr/bin/python3.7

import numpy as np
from time import time

with open('../teste_saida_4.txt', 'r') as f:
   lines = f.read()
lines=lines.replace('\n',"")
lines=lines.replace(' ',"")
lines=lines.replace('[',"")
lines=lines.replace(']',"")
lines=list(filter(lambda row: row!=',' and row!='', lines.split("'")))
a = np.array(lines)
a = a.astype(int) ## Conversão de texto para inteiro

with open('../teste_saida_44.txt', 'r') as f:
   lines = f.read()
lines=lines.replace('\n',"")
lines=lines.replace(' ',"")
lines=lines.replace('[',"")
lines=lines.replace(']',"")
lines=list(filter(lambda row: row!=',' and row!='', lines.split("'")))
b = np.array(lines)
b = b.astype(int) ## Conversão de texto para inteiro


#start_time=time()
b = np.array(b[0:250])

mse = np.ndarray((len(a) - len(b) + 1))

for i in range(mse.size):
   mse[i] = np.square(np.subtract(a[i:i+len(b)],b)).mean()

print(mse.min())
#print(time()-start_time)
