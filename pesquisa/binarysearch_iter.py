lista = [1,2,3,4,5,6,7,8,9,10,11,11,12,100]

def bsitera(lista, n):
    inicio = 0
    fim = len(lista)-1
    meio = (inicio + fim) // 2
    while  inicio < fim:
        if n > lista[meio]:
            inicio = meio + 1
        if n < lista[meio]:
            fim = meio
        if n == lista[meio]:
            return meio
        meio = (inicio + fim) // 2
        
    return -1



print(bsitera(lista, 5))