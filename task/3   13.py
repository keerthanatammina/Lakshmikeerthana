def fib(n):
    a,b=0,1
    while a<n:
        print(a,end='\n')
        #a=a+1
        #b=b+a
        a,b=b,b+a
fib(80)
