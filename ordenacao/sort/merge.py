def intercala(lista, inicio, meio, fim):
    i = inicio
    j = meio
    aux = []
    while i<meio and j<fim:
        if lista[i]<lista[j]:
            aux.append(lista[i])
            i+=1
        else:
            aux.append(lista[j])
            j+=1
    # fim while -> i < meio ou j < fim
    while i<meio:
        aux.append(lista[i])
        i+=1
    while j<fim:
        aux.append(lista[j])
        j+=1
    return aux

L = [0,1,6,20,4,5,7,10]
print(L)
L_O = intercala(L, 0, 4, 8)
print(L_O)
# L_O = [0,1,4,5,6,7,10,20]