
qtd=0
def intercala(lista, inicio, meio, fim):
    i = inicio
    j = meio+1
    
    aux = []
    
    while i<=meio and j<=fim:
        global qtd
        qtd+=1
        if lista[i]<lista[j]:
            aux.append(lista[i])
            i+=1
        else:
            aux.append(lista[j])
            j+=1
    # fim while -> i < meio ou j < fim

    while i <= meio:
        aux.append(lista[i])
        i+=1
    while j <= fim:
        aux.append(lista[j])
        j+=1
    
    #print('----------')
    #print(lista)
    #print(aux)
    for k in range(len(aux)):
        lista[inicio+k] = aux[k]
    #print(lista)
    
def _merge_sort(inicio, fim, lista):
    global qtd
    qtd+=1
    if inicio != fim:
        meio = (inicio+fim)//2
        _merge_sort(inicio, meio, lista)
        _merge_sort(meio+1,fim, lista)
        intercala(lista, inicio, meio, fim)

def merge_sort(L):
    _merge_sort(0,len(L)-1,L)    

L = []
n=10**6

import random
for i in range(n):
    L.append(random.randint(0,600000))

merge_sort(L)

print("ordenada")
print(qtd)




