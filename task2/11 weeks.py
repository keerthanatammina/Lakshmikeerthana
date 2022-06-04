b=int(input("enter a number"))
a={1:"monday",2:"tuesday",3:"wednesday",4:"thursday",5:"friday",6:"saturday",7:"sunday"}
for i in a:
    if i==b:
        print(a.get(i))
        break
else:
    print("invalid")
        
            

