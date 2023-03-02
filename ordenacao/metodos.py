
def selection_sort(L):
    cont = 0
    for i in range(0, len(L)-1):
        menor = i
        for j in range(i+1, len(L)):
            if L[j] < L[menor]: # L[menor] > L[j]
                # atualizar o menor
                menor = j
            cont+=1
        # fim do for j
        #if i != menor:
        L[i], L[menor] = L[menor], L[i]
        #print(L)
    # fim do for i
    #print(f'Comparei {cont} vezes')
    return L

def selection_sort_rec(L, indice):
    # caso base
    print(L)
    if indice >= len(L)-1:
        return L
    menor = indice
    for j in range(indice+1, len(L)):
        if L[j] < L[menor]: 
            menor = j
    # fim do for j    
    L[indice], L[menor] = L[menor], L[indice]
    return selection_sort_rec(L, indice+1)

def bubble_sort(L):
    indice = len(L)-1
    cont = 0
    while indice > 0:
        for i in range(0, indice):
            #print(L)
            if L[i] > L[i+1]:
                # faz a troca
                cont+=1
                L[i], L[i+1] = L[i+1], L[i]
            #input()
        indice -= 1
    print(cont)
    return L 

L = [12,10,8,6,4,2]
#print(L)
#print(selection_sort(L))
#L.sort()
bubble_sort(L)
print('Ordenado')