def vow(*n):
    '''demo of func'''
    a=[]
    for i in n:
        if i=='a' or i=='A' or i=='e' or i=='E' or i=='I' or i=='i' or i=='o' or i=='O' or i=='u' or i=='U':  
            a.append(i)
    print(a)
    print(f"length is {len(a)}")
n=input("enter")
vow(*n)
