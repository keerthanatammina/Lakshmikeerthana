a=["i","you"]
b=["play","love"]
c=["cricket","hockey"]
def sen(*d):
    #demo for func
    print(d)
    for i in range(len(a)):
        for j in range(len(b)):
            for k in range(len(c)):
                print(a[i],b[j],c[k])
sen(a,b,c)              
'''def sen():
    a=[(i,j,k) for i in ["i","you"] for j in ["play","love"] for k in ["hockey","cricket"] if i!=j and j!=k and k!=i]
    print(a)
sen()'''        


    
    
    
