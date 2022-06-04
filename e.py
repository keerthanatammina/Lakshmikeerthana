from employee import *
basic=float(input("enter"))
gross=basic+ha(basic)+hra(basic)+ta(basic)#cal gross salary
print("gross salary is %.2f"%gross)
nett=gross-pf(basic)-itax(gross)#cal .nett salary
print("final take home is %.2f"%nett)
