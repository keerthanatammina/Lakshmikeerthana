#creating a file
a=open("ta.txt","a")
b=["Zen of Python","Ester eggs"]
a.write("\n".join(b))
a.close()
'''
import os
#from os import *
def new(file):
    if os.path.isfile(file):
        with open(file) as file:
            return file.read()
    else:
        return None
print(new("bingo.txt"))

    a=open("ta.txt","a")
    return a
b=[str(x) for x in input("enter").split(',')]
a.write("\n".join(b))
a.close()
'''
