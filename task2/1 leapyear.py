year=int(input("enter a year"))
if year%4==0 and (year%100!=0 or year%400==0):
    print(f"year is a leapyear")
else:
    print(f"is not leapyear")

   

    
