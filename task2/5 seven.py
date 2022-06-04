a=[]
for i in range(1,201):
    if i%7==0 and i%5!=0:
        #print(i,end=',')
        a.append(str(i))
print(a)
print(','.join(a))     
        
        
