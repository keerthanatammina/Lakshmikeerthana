def roll(n):
    a=[int(x) for x in input("enter").split(',')]
    print(type(a))
    if n in a:
        print("student is present")
    else:
        print("absent")
roll(34)




'''enter23,34,40,45,56
<class 'list'>
absent'''
