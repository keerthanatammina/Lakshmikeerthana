n1=input("enter a metric");n2=float(input("enter a value"))
inch=2.54;centi=1/inch
if n1 == "inch" or n1 =="inches":
   print(float(n2*inch))
elif n1=="cms" or n1 == "centimetres":
    print(float(n2*centi))
else:
    print("Wrong input enter")
    
