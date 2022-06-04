value=input("enter a value")
upper=0
lower=0
for each_char in value:
    if each_char.isupper():
       upper+=1
    elif each_char.islower():
        lower+=1
    else:
        pass
print(f"lowercase letters are {lower}")
print(f"upper cae letters are{upper}")

