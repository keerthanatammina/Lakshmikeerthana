a=input("enter")
if len(a)<3:
    print(a)
elif a[-3:]=="ing":
    print(a+"ly")
elif len(a)>=3:
    print(a+"ing")
    
    
