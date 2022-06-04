a=input("enter")
a1=['jan','march','may','july','aug','oct','dec']
a2=['feb']
a3=['april','june','sep','nov']
if a in a1:
    print("31 days")
elif a in a2:
    print("28 or 29 days")
elif a in a3:
    print("30 days")
else:
    print("invalid ")

