lista = ["A","C","F", "B", "C", "I"]


def sequencial(vetor,chave):
    print(vetor)
    for i in range(len(vetor)):
        if chave == vetor[i]:
            return i
    return -1


print(sequencial(lista,"J"))