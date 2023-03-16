def intercala(lista, inicio, meio, fim):
    i = inicio
    j = meio+1

    aux = []
    
    while i<=meio and j<=fim:
        
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
    
def merge_sort(inicio, fim, lista):
    if inicio != fim:
        meio = (inicio+fim)//2
        merge_sort(inicio, meio, lista)
        merge_sort(meio+1,fim, lista)
        intercala(lista, inicio, meio, fim)
    

L = [2,3,4,10,5,15,18,20,12,13]
print(L)
merge_sort(0,9,L)
print(L)




