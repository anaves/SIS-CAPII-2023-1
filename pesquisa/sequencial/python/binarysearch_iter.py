lista = [1,2,3,4,5,6,7,8,9,10,11,11,12,100]

def bsitera(lista, n):
    inicio = 0
    fim = len(lista)
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


def bsrecur(lista, inicio, fim, chave):
    if inicio > fim:
        return -1
    else:
        meio = (inicio + fim) // 2
        if chave > lista[meio]:
            return bsrecur(lista, meio + 1, fim, chave)
        if chave < lista[meio]:
            return bsrecur(lista, inicio, meio -1, chave)
        else: 
            return meio

def chamabsrecur(lista, chave):
     return bsrecur(lista, 0, len(lista), chave)

print(chamabsrecur(lista, 100))

# print(bsrecur(lista, 0, len(lista) - 1, 5))