n1=int(input("enter a n1"));n2=int(input("enter a n2"));prime=True
for i in range(2,n1,n2):
    if (n1 and n2)%i==0:
       prime=False
    break
if prime:
    print(f" {n1} and {n2} is prime")
else:
    print(f" {n1} and {n2} is not prime")
