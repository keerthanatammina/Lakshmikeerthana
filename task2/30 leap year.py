a=[]
for i in range(1900,2102):
    if i%4==0 and (i%100!=0 or i%400==0):
        print(i)
        a.append(str(i))
print("length","=",len(a))

        
        
        
    
