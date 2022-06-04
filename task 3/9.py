import random
def new(fname):
    a=open(fname).read().splitlines()
    return random.choice(a)
print(new("style.txt"))

