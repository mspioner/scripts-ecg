#!/usr/bin/python3
import json, re, os
import numpy as np
from time import time

def get_file(file):
    blockchain_get_data(file)
    with open(str(file)) as json_file:
        dados = json.load(json_file)
        return get_data(readlines(dados))

def get_file2(file):
    with open(str(file)) as json_file:
        dados = json.load(json_file)
        return get_data(readlines(dados))


def readlines(dados):
    list = []
    for n1, n2 in dados.items():
        if re.findall("[a-zA-Z]+", n2):
            pass
        else:
            list.append(n2)
    #print(len(list))
    return list

def get_data(list):
    list2 = list[79:829]
    maior = max(list2, key=int)
    posicao = (list.index(maior))
    posteriores = list[posicao:(posicao+170)]
    anteriores = list[(posicao-80):posicao]
    tudo = anteriores + posteriores
    return tudo

def ecg_compare(r1,r2):
    lines = r1
    a = np.array(lines)
    a = a.astype(int) ## Conversão de texto para inteiro
    lines = r2
    b = np.array(lines)
    b = b.astype(int) ## Conversão de texto para inteiro


    #start_time=time()
    b = np.array(b[0:250])

    mse = np.ndarray((len(a) - len(b) + 1))

    for i in range(mse.size):
       mse[i] = np.square(np.subtract(a[i:i+len(b)],b)).mean()

    print(mse.min())

def blockchain_get_data(pessoa):

    d = os.system("./ssh.sh -f" + pessoa)
    return d

r1 = get_file(input("Registro 1: "))
#print(r1)
start_time=time()
r2 = get_file2(input("Registro 2: "))
#print(r2)
ecg_compare(r1, r2)


tempo=int(time()-start_time)
print(str(tempo)+" segundos para autenticação")
