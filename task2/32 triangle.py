num1=int(input("enter a num"));num2=int(input("enter a num"));num3=int(input("enter a num"))
if num1==num2 and num1==num3 and num2==num3:
    print("equilateral triangle")
elif num1!=(num2 and num3) or num2==num3:
    print("isoceless triangle")
elif num1!=num2 and num2!=num3 and num1!=num3:
    print("scalene triangle")
