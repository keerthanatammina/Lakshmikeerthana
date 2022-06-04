def new(n):
    s=0
    for i in range(1,n+1):
        if i%3==0 or i%5==0:
            s=s+i
            print(i)
    print(s)
a=int(input("enter a number"))
new(a)
