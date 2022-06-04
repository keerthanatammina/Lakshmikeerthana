n=int(input("enter a number"))
sum=0;count=0
for i in range(1,n+1):
    sum=sum+i;count=count+1;avg=sum/count
print(f"average={avg},total={sum}")
