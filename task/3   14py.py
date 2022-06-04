def val(a):
    '''deom for fun'''
    b={'upper':0,'lower':0}
    #upper=0
    #lower=0
    for i in a:
        if i.isupper():
            b['upper']+=1
        elif i.islower():
            b['lower']+=1
    print(b)
    print(f"upper are",b['upper'])
    print(f"lower are",b['lower'])
a=input("enter")
val(a)



        
            
