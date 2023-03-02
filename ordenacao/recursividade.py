
def contagem_regressiva_ite(n):
    for i in range(n,0,-1):
        print(i)
    print('Fogo!')

def contagem_regressiva(n):
    # caso base
    print(f'---in: {n}')
    if n == 0:
        print('Fogo')
    else:
        print(n)
        contagem_regressiva(n-1)
    print(f'---out: {n}')

def fatorial_iterativo(n):
    # se n=5--> 5! = 5*4*3*2*1
    r = 1
    for i in range(1,n+1):
        r = r*i
    return r

def fatorial_recursivo(n):
    # caso base
    if n==0:
        return 1
    else:
        return n*fatorial_recursivo(n-1)


fat = fatorial_iterativo(1000)
#fat = fatorial_recursivo(1000)
print(f'{5}! = {fat}')
#contagem_regressiva_ite(100000)