import datetime
from datetime import *
d,m,y=(int(x) for x in input("enter").split(':'))
a=date(y,m,d)
print(a)
print(a.strftime("month is %B"))
print(a.strftime("week of the day is %a"))



