lista = ["A","C","F", "B", "C"]


def sequencial(vetor,chave):
    print(vetor)
    for i in range(len(vetor)):
        if chave == vetor[i]:
            return i
    return -1

def sequencial_todos(vetor, chave):
   # vamos implementar uma solucao!
   pass
print(sequencial(lista,"C"))