def fib(n):

    if n == 1 or n == 2:
        #print(n)
        return 1
    else:
        a = fib(n-1)
        b = fib(n-2)
        #print(a+b)
        return a+b
        # return fib(n-1) + fib(n-2)

def fib2(n):
    for i in range(1,n+1):
        print(fib(i))

fib2(10)