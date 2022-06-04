def a(speed):
    if speed<70:
       print("riding well")
    elif speed>=70:
        points=(speed-70)//5
        print(f"demerit point is {points}")
        if points>=10:
           print("license rejected")
speed=int(input("enter"))
a(speed)


            
            
