
#21-05-2022
#COMPHREHENSIONS

#LIST METHOD
#For int
'''a=[int(x) for x in input("enter").split(',')]
print(a)
print(type(a))'''

#For Float
'''a=[float(x) for x in input("enter").split(',')]
print(a)
print(type(a))'''

#FOR THREE FOR LOOP CONDITIONS   IMPORTANT
'''a=[(i,j,k) for i in ["i","you"] for j in ["play","love"] for k in ["hockey","cricket"] if i!=j and j!=k and k!=i]
print(a,end="/n")'''

#for str
'''a=[str(x) for x in input("enter").split(',')]
print(a)
print(type(a))'''

#in list way squares of even nos
'''a=[x**2 for x in range(1,11) if x%2==0]
print(a)'''

#in tuple way
'''a={x**2 for x in range(1,11) if x%2==0}
b={x for x in range(1,11) if x%2==0}
print(a)
print(b)
c=dict.fromkeys(b,a)
print(c)'''

#in dict
'''a={x:x**2 for x in range(1,6)}
print(a)'''

#conversion of tuple into list :
'''a=list(x for x in input("enter").split(','))
print(a)'''

#to get reverse order

'''for i in range(10,0,-1):
    print(i)'''

# to get step order

'''for i in range(1,6,2):
    print(i)'''

#to get sort method

'''a=["bab","app","pop","queen","lmeon"]
print(a.sort())'''

# concatenate without using '+'
'''a = input("Enter a word")
print(a)
if len(a) > 3:
    #if a[-3:] == "ing":
    if a.endswith('ing'):
        print(a[:-3] + "ly")
        #print(a + "ly")
    else:
        print(a + "ing")
else:
    print(a)'''


#FUNCTIONS
#TYPES - BULIT IN FUNCTIONS AND USER DEFINED FUNCTIONS


#Fibonacci sequence
'''def fib(n):
    a,b=0,1
    while a<n:
        print(a,end=' ')
        a,b=b,a+b
fib(5045690)'''

#Arguments:
#types
# 1.POSITIONAL ARGUMENTS
# 2.DEFAULT ARGUMENTS
# 3.KEYWORD ARGUMENTS
# 4.VARIABLE LENTH ARGS(*ARGS)
# 5.(**ARGS)

#  1. POSITIONAL ARGUMENTS

#1
'''def code(a,b):
    """Postn args demo"""
    return a+b
print(code(2,5))
print(code('code','gnan'))
print(code([1,4],[2,5]))'''

#2
'''def pol(a,b=34):
    return a+b
print(pol(12))'''

#2. KEYWORD ARGUMMENTS
'''def grocery(items,price):
    """Keywrd args demo"""
    print("Item is %s"%items)
    print("Price is %.2f"%price)
grocery(price=35,items="Bread")
#grocery(Price=25,items="jam")'''

#3.  DEFAULT ARGUMENTS

'''#def grocery(items,price=25):
#def grocery(items="KFC",price): #non-default always follows default
def grocery(items="KFC",price=523):
    """Keywrd args demo"""
    print("Item is %s"%items)
    print("Price is %.2f"%price)
grocery("Bread",35)
grocery("jam",76)
grocery()'''


#  4*ARGS

#1.args(*)
'''a=[1,2,3,4]
print(a)
print(*a)
print(type(a))
for i in a:
    print(i,end='\n')
b=[1,2,3,*a]
print(b)'''

#2.*args
'''def pol(*args):
    for i in args:
        print(i,sep=',')
pol(1,2,3,4,5)'''

#3.*args
'''def pol(a,*b):
    d=0
    for i in b:
        d=d+i
    return d+a
print(pol(2,3,4.5,67,89))'''

               #(OR) ANOTHER METHOD      IMPORTANT
'''a=int(input("enter"))
b=[int(x) for x in input("enter").split(',')]
print(type(b))
def pol(a,*b):
    d=0
    print(type(b))
    for i in b:
        d=d+i
    return d+a
print(pol(a,*b))'''

#4. *args
#Variable length arguments ->Number of arguments are not fixed,we
#use * as symbol to represnt,where the data is internally stored in a tuple

'''a = [1,5,2,6,3,12]
print(a)
print(a[-3]) #Indexing
print(a[3])
print(a[2:])
print(a[2:3]) #the outcome is always a list
for i in a:
    print(i,end=' ')
print(*a) #* is used to unpack the elements from a collection
b = [2,4,5,6]
#c = [a,b]
#c = a+b #merging
c = [*a,*b]
print(c)
print(len(c))'''

# UNPACKING ARGUMENTS     IMPORTANT

'''def pol(a,b,c,d,e):
    print(a,b,c,d,e)
lst=[1,2,3,4,5]
tup=(1,2,3,4,5)
pol(*lst)
pol(*tup)'''


# 5.**KWARGS
#IT FORMS DICTIONARY

#1
'''def pol(name="sak",age="siv"):
    print(name,age)
d={'name':4445,'age':556}
pol(d)
pol(*d)
pol(**d)'''

#2 form for dict
'''def pol(a,**b):
    print(type(b))
    for c,d in b.items():
        print(f"key = {c}")
        print(f"values= {d}")
pol(12,name="ask",ag=34,sd="ert")'''

#3 dict
'''def new(*a,**b):
    d=0
    for i in a:
        d=d+i
    print(d)
    for i,j in b.items():
        print(f"key is {i}")
        print(f"values is {j}")
new(1,2,3,4,name="codegnan",place="vij",age=23)'''

#4 dict
'''a=[1,2,3,4]
b={a:2,b:4}
def new(*a,**b):
    for i in a:
        print(i)
    for j in b:
        print(j)
new(*a,**b)'''

#GLOBAL AND LOCAL VARIABLES       IMPORTANT

#1 EAXMPLE
'''a="saketh"
def check():
    b=25
    b+=4
    print(b)
    a="code"
    print(a)
check()
print(a)
print(b)'''

#2 Example USING global FUNCTION
#When user want to use global variable inside the function and even access it
#outside the function we need to use global keyword
'''a=4
def check(*a):
    global a
    print(a)
    a+=25
    print(a)
check(1,2,3,4,5)
print(a)'''

#local variable scenario
'''a=34
def check1():
    """using local and global variables"""
    global a,b
    print("Value of a inside is",a)
    a = a**2
    print("Updated value of a is",a)
    b = 15 #local variable
    b = b+a
    print("Value of b is",b)
check1()
print("Value of a outside is",a)
print("Value of b outside is",b)'''

# IMPORTANT
'''c = [1,4,5,6]
d = {'bts':7,'army':1000}
#def new(*a):
#def new(**a):
def new(*a,**b):
    """sample demo"""
    print(a)
    print(type(a))
    print(b)
    print(type(b))
    for i in a:
        print(i)
    for i in b:
        print(b[i]) #b[i] this array is used to represent the values from a key dictionary
#new(15,2,6,3)
#new(1,2,4,5,6,7,8,9)
#new(**a)
#new(*a)
#new(*a,**b)
new(*c,**d)'''

#23-5-2022

#GENERATOR FUNCTION
#A Generator is also a Function which can be used as an Iterator(values can be looped upon)
#A Function becomes a Generator when we want to produce group of values

#No Tuple Comprehension -->Tuples are Immutable
#A Generator is created
'''a = (x*2 for x in range(1,11))
print(a)
#multiple ways to get values out of generator but only once
#print(*a)
for i in a:
    print(i)
print(tuple(a)) #once values are read(taken out of generator) cannot be iterated again
print(type(a))'''

#IMPORTANCE OF WHILE LOOP
#With the while loop we can execute a set of statements as long as a condition is true.
# 1.
'''i = 1
while i <= 6:
  print(i)
  i += 1''' # to iterate the loop for until we want the output

#2.YIELD KEYWORD
#Yield is a keyword in Python that is used to return from a
#function without destroying the states of its local variable
'''e,f = [int(x) for x in input("Enter the values").split(',')]
print(e,f)
#print numbers between given inputs
def check(a,b):
    """importance of yield"""
    #i=0 #counter variable
    while a<=b:
        yield a
        a=a+1 #addition assignment operator
    #return a
        #yield a
print(*check(e,f))
c = check(e,f)
print(c)
print(*c)'''
#print(tuple(c)) #we get empty tuple
#print(__name__)

#DIFFERENCE BETWEEN RETURN AND YIELD
#Yield is generally used to convert a regular Python function into a generator.
#Return is generally used for the end of the execution and
#“returns” the result to the caller statement.

#return
'''def n(a):
    print(a*2)
    return a
n(4)'''

#def n():
    #doc'''
     #'''return "a"
#print(n())'''

#yield

#1.
#def n():
    #'''doc'''
    #yield "a"
#print(n())'''

#2.
'''def n(a):
    print(a*2)
    yield a
    b=45
    c=a+b
    yield c
n(4)'''

#3.
#def new(a):
'''def new():
    """demo for generators"""
    return "A" 
    return "B"
    return "C" 
    #yield "A"
    #yield "B"
    #yield "C" 
print(new(str(25)))
#print(new())
f = new() #Assgngn Function to a variable
print(next(f))
print(next(f))
print(next(f))
print(next(f)) #iterates value one by one andstops at the end of iterator'''


#creation and even pass them as arguments for built-in functions (filter,map)
'''
We will be using lambda keyword
Syntax:

lambda argument(s) : expression '''

#Function to compute 5*x+5 when x=2
'''def f(x):
    """Sample math function"""
    return 5*x+2
print(f(2))
print(f.__doc__)'''

             #(OR)

'''a = lambda x:5*x+2
print(a(5))
print(type(a))'''

                #(OR)
'''b = lambda x:x.title()
print(b('codegnan saketh'))'''

'''a=[1,5,6,8]
b=[7,2,3]
c=list(zip(a,b))'''


'''def a(n):
    for i in range(1,n+1):
        b=i/n
        print(b)
        continue
a(9)
print(sum(float(9)))'''

#map()
'''a=dict(map(float,input("enter").split(',')))
print(a)'''

 #Accepting two lists of

#MOdules
#def check():
#demo for dunder methods'''
#if __name__=="__main__":
        #''' print("script is run as a program")
     #else:
         #print("this script is run as a module")
'''check()
print(__name__)
a={"names":['codegnan','saketh','python'],'place':'vij'}'''

#25-05-22
#time module

#epoch it is the point where the time starts
'''import time
epoch=time.time()
#print(epoch)
for i in range(1,11):
     print(i)
time.sleep(1) #sleep function
end=time.time()
#print(end-epoch,"seconds for running for loop")

#converting epoch time into date and time
a=time.time()
print(a)
'''

'''v=time.localtime()
print(v)

#to get date
date=v.tm_mday
print(date)

# to get month
month=v.tm_mon
print(month)

#to get year
year=v.tm_year
print(year)
print(f"date is{month}:{date}:{year}")

#to get minutes
min=v.tm_min
print(min)

#to get hour
hour=v.tm_hour
print(hour)

#to get sec
sec=v.tm_sec
print(sec)
print(f"time is {hour}:{min}:{sec}")
'''
'''
#ctime
e=time.ctime(a)# here its converting local time into string format by using ctime()
print(e)
'''

#DATETIME MODULE
#python program to find current date time
import datetime
#print(dir(datetime))
from datetime import *
'''
n=datetime.now()#Now() method is used to get datetime class object
print(n)
print(n.year)
print(n.month)
print(n.min)
     
#to get datetime class
t=datetime.today() #to get todays current date time
print(t)

#to get time class object
tmd=time.today()#getting time from time module
print(tmd)
#THERE IS A LOT OF DIFFERENCE BETWEEN TIME AND DATETIME MODULES

#DATETIME FUNCTIONS
#combine()
#1.METHOD
d=date(2022,5,25)
print(d)
t=time(12,30)
print(t)
c=datetime.combine(d,t)
print(c)

#2.METHOD
d=datetime(2022,5,26,5,30,26)
print(d)

#replace()
e=d.replace(2023,6,6)
print(e)
print(type(e))

    
#formatt datetime
a=datetime.today()
print(a)

#here in format methods we are using strftime() and strptime() functions
#strftime()
#%d-
#%b-
#%B-
#%w-
#%Y-
#%a-
#%A-

c=a.strftime("%d,%w,%Y")
print(c)
e=a.strftime("%a,%A,%b")
print(e)

#strptime()


#split()


#TIMEDELTA()
#it is used to know the future time and date

#ex program
d=datetime(2022,5,26,10,30,45)
print(d)
period=timedelta(days=10,hours=5,minutes=45)
print("new date an time is",d+period)


#ex program to know the date of births of 2 persons and who is older one
d1=[int(x) for x in input("enter").split('-')]
print(d1)
d2=[int(x) for x in input("enter").split('-')]
print(d2)
if d1==d2:
     print("both are same aged persons")
elif d1>d2:
     print("d1 is younger than d2")
else:
     print("d2 is younger than d1")
     '''

#CALENDAR MODULE
'''
import datetime
from datetime import *
a=time.now()
print(a)
print(f"date is {n.date}:{n.month}:{n.year}")
'''
import time
d=date(2022,5,26)
print(d)











         

       
