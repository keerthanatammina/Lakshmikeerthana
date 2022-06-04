a=[str(x) for x in input("enter").split(",")]
print(a)
words=[]
for i in a:
    words.append((len(i),i))
print(words)
words.sort()
print(words)
print("longest words",words[-1][1])
print("length of longest word is",words[-1][0])

    


