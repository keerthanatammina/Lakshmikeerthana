
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


#ANONYMOUS FUNCTIONS
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
print(f.__doc__)

             #(OR)

a = lambda x:5*x+2
print(a(5))
'''

                #(OR)
'''b = lambda x:x.title()
print(b('codegnan saketh'))


#2.
a=(lambda x:x**2)
print(a(5))
#print(list(a))
'''
#ZIP MODULE
'''
a=[1,5,6,8]
b=[7,2,3]
c=list(zip(a,b))
print(c)'''


'''def a(n):
    for i in range(1,n+1):
        b=i/n
        print(b)
        continue
a(9)
print(sum(float(9)))

#filter
#filter is used for only decision statements by analysis
#1.
b=[int(x) for x in range(1,21)]
a=list(filter(lambda x:x%2==0,b))
print(a)

#2.
b=(int(x) for x in range(1,201))
a=tuple(filter(lambda x:x%3==0 and x%5==0 and x%12!=0,b))
print(a)

#map()
#every element from a collections and gives result
#accepting multiple integer values from user
#example
#1.
a,b=[map(int,input("enter").split(','))]
print(a,b,sep=",")

#2.
c=list(map(lambda x,y:x+y))
print(c)

#using map and filter()
a=list(map(lambda x:x**2,filter(lambda x:x%10==0,range(1,51))))
print(a)

#2.
a=tuple(map(lambda x:x/5,filter(lambda x:x%4==0,range(1,51))))
print(a)

#3.
a=dict(map(float,input("enter").split(',')))
print(a)


 #Accepting two lists of

#MOdules
def check():
     #demo for dunder methods
     if __name__=="__main__":
         print("script is run as a program")
     else:
         print("this script is run as a module")
check()
print(__name__)
#name and __ are called dunder
#every python file is named as __name__=="__main__" by defaulty
#a module is a python file consisting of variables,functions and classes so on

#using as keyword (aliasing)
#returning false names or temporary names

#we are using * to get multiple functions,attributes from modules

#COMPREHENSIONS
#1.
a={i for i in range(1,21) if i%3==0}
print(a)

#2.
a=[i for i in range(1,31) if i%2==0 and i%5!=0]
print(a)

#3.
a=["codegnan" if i%2==0 and i%4==0 else "python" if i%5==0 else "saketh" if i%3==0 else i for i in range(1,51)]
print(*a,sep="\n")


#25-05-22
                                         #time module

#epoch it is the point where the time starts
import time
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

#to get LOCAL TIME
v=time.localtime()
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

#ctime
e=time.ctime(a) # here its converting local time into string format by using ctime()
print(e)


#DATETIME MODULE
#python program to find current date time
import datetime
#print(dir(datetime))
from datetime import *

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
import datetime
from datetime import *
a=datetime.today()
print(a)

#here in format methods we are using strftime() and strptime() functions
#strftime()
#%d-day of month
#%b-month as time
#%B-month full name
#%w-week day as derival name
#%Y-4 year digit no
#%a-weekday as abbreviation
#%A-weeekday full name

c=a.strftime("%d,%w,%Y")
print(c)
e=a.strftime("%a,%A,%b")
print(e)

b=a.strftime("%m,%b,%a,%A,%B,%d")
print(b)

#strptime()
import datetime
from datetime import *
value="26 dec 2012"
s=datetime.strptime(value,"%d %B %Y")
print(s)

#split() 
import datetime
from datetime import *
d,m,y=[int(x) for x in input("enter").split(':')]
dt=date(d,m,y)
print(dt)
print(dt.strftime("%d"))
print(st.strftime("%a"))


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
     

#CALENDAR MODULE

import datetime
from datetime import *
a=time.now()
print(a)
print(f"date is {n.date}:{n.month}:{n.year}")

import time
d=date(2022,5,26)
print(d)


#25-5-2022

#SYS AND OS MODULE
#example
#creating an employee module in calculate gross salary from allowances and nett salary
#Houserent allowance
def hra(basic):
    """HRA is 10% of basic salary"""
    hra=basic*10/100
    return hra

#health allowance
def ha(basic):
    #ha is 15% of basic salary
    ha=basic*15/100
    return ha

#travel allowance
def ta(basic):
    # ta is 12% of basic salary
    ta=basic*12/100
    return ta

#pf
def pf(basic):
    #pf 5% of basic salary
    pf=basic*5/100
    return pf

#income tax
def itax(basic):
    #itax 8% of basic salary
    itax=basic*8/100
    return itax
#output
#to get output it is (e.py)in another python file

#system module
import sys
#print(dir(sys))
#to check python version
b=sys.version
#print(b)
#information
c=sys.version_info
#print(c)
d=sys.path # will complete python installed path
#print(d)
#print(*d)
#for i in d:
    #print(i)
#to open current file path
#print(sys.argv)

#OS module

import os
#print(dir(os))
print(os.path)#it gives information about how path to be given
print(os.getcwd())#to get current working directory

#module used in os are:
# 1.getcwd()- to get current working directory
# 2.chdir() - to change the directory name
# 3.mkdir() -to create a new folder in mtfiles mnager
# 4.files- to create various files click right click of a mouse to get text documents
# 5.listdir()-to represent the all files which is present in the partiuclar directory that may be a python file or notepad file
# 6.is.file()-generally it is used to check whether the file is present or noy in such directory(os.isfile())
# 7.join() - to join some paths of a files(os.path.join)
# 8.split()- to split the path files(os.path.split(''))
# 9.rename- to rename the old filename to a new file name(os.rename('',''))
# 10.remove()-to remove the file in any directory(os.remove(','))
# 11. with and as keywords
#ex for with (mostly it is used to
with open("nweer.txt","w") as f:
f.write("\n".join(lines))

#26-5-22

#RANDOM
import random
import time
a=random.random()#it gives random values

#print(a)
#OTP GENERATION
#randint()
b=random.randint(1,10)
for i in range(20):
    time.sleep(1)
    print(random.randint(10000,99999))


#randomrange
for i in range(10):
    print(random.randrange(10,100,2))

#random choice
a=random.choice('saketh')
print(a)
   #(or)
a=random.choice([1,2,3,4,5,67])
print(a)

#random shuffle
a=(1,2,3,4,5)
b=random.shuffle(a)
print(b)

                                         #files

#write,read,append,X(crete new file)
a=open('qwert.txt','w')
#print(a)
a.write("hello world")
a.close()

b=open('kajal.txt','a')#here a is append and this append is also used to  create a new file
b.write("hii kajuuu")
b.close()

b=open('anu.txt','a')
c=['\tpython','codegnan','java']
b.writelines(c)
b.close()
'''
    
#FILES I/O SYSTEM
#to communicate with the computer
#IO - is used to store the data in files
#we have two types of files are : (1) text files
                                  #(2) binary files
#all program files are text files
# all images,videos,jpg,mp3,mp4,audio,store text are binary files


#28-5-2022
#NUMPY AND ARRAYS
#numpy can install in cmd prompt or else in jupyter notebook
import array as ar
help(array)

a=[1,2,3,4]
b=ar.array('i',a)
print(b)
#type(a) - list
#type(b) - array.array

import numpy as np
b=np.array(a)
print(b)

#here we have five main ones are: (#for a =[1,2,3,4])
# 1. a.ndim - to get the dimension of an arrays
# 2. a.shape- to get the shape of a array
# 3. a.size- to get the number of elements present in an array
# 4. len- length of array
# 5. type- to know which data type of a

# in numpy arrays  -->axis 0 -> rows,axis 1->colums
#IN ARRAYS THE DATA IS FIRST STORED IN FROM HORIZONTAL TO VERTICALLY
    

#difference between arrays and lists -->memory efficinet -->easy and faster to exceute -->element wise operations
#Memory comparsion
a=list(range(1000))
#print(a)
import sys
b=sys.getsizeof(77)*len(a) #getsizeof -->return the size of object in bytes
print(b)

#ARANGE()in arrays
b=np.arange(1000)
b

b.size*b.itemsize #itemsize-->returns memory occupied for objec         

#IN LIST FORMAT (#WE USED RANGE FUNCTION)       
#faster to exceute
import time
l1=list(range(100000))
l2=list(range(100000))
start=time.time()
l3=list(map(lambda x,y:x+y,l1,l2))
end=time.time()
print((end-start)*1000)#1000 is used to convert into milli seconds


#IN ARRAY FORMAT WE ARE USING ARANGE FUNCTION FOR np
import time
l1=np.arange(100000)
l2=np.arange(100000)
start=time.time()
t=l1+l2
end=time.time()
print((end-start)*1000)#1000 is used to convert into milli seconds


#to creating a matrix in array
a=np.array([[1,2,3,4,5],
           [8,7,8,9,9],
           [3,5,6,7,8]])
print(a)

#indexind and slicing
a[0]
a[0:2]
a[0][3] #subindexing


#accessing column wise data
a[0:,0]
a[0:,0:2]#array[rows,columns]
a[0:1,0:3]
a[1:,1:3]




