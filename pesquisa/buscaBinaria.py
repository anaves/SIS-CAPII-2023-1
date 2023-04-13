letras = ["A","B","C","D","F","G","H"]

def _busca_binaria(lista, inicio, fim, chave):
    if inicio > fim:
        return -1 # elemento nao esta na lista
    else:
        meio = (inicio+fim)//2
        if lista[meio].upper() == chave.upper():
            return meio
        elif chave.upper() > lista[meio].upper():
            return _busca_binaria(lista, meio+1, fim, chave)
        else:
            return _busca_binaria(lista, inicio, meio-1, chave)

def busca_binaria(lista, chave):
    return _busca_binaria(lista, 0, len(lista)-1, chave)

index = busca_binaria(letras,"b")

print(index)