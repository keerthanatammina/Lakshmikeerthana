def max(a,*b):
    '''description of function'''
    if len(a)==len(b):
        print(f"{a} and len is {len(a)}")
        print(f"{b} and len is {len(b)}")
    elif len(a)>len(b):
         print(a,len(a))
    elif len(a)<len(b):
         print(b,len(b))
    else:
        pass
a=input("enter")
b=input("enter")
max(a,*b)
