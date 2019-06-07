#!/usr/bin/python3
import json, re

def main():
    with open('../Person_2/leitura_1_json copy.txt') as json_file:
        dados = json.load(json_file)
        get_data(readlines(dados))
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
    print (tudo)
#
#
main()
