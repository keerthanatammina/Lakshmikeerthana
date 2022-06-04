import datetime
from datetime import *
d1,m1,y1=(int(x) for x in input("enter").split("-"))
dt1=date(y1,m1,d1)
print(dt1)
d2,m2,y2=(int(x) for x in input("enter").split("-"))
dt2=date(y2,m2,d2)
print(dt2)
if dt1>dt2:
    print(dt1-dt2)
else:
    print(dt2-dt1)













