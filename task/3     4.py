#n=int(input("enter"))
#a=[int(x) for x in range(1,6)
b=0
a=[int(x) for x in input("enter")]
for i in range(1,a+1):
    b+=a/(a+1)
print(list(b))

#a=int(input("enter"))
'''while a<=6:
    b=float(a/a+1)
print(sum(b))'''


def n(a):
    count=0
    for i in range(1,a+1):
        count+=i/(i+1)
    print(count)
n(6)
