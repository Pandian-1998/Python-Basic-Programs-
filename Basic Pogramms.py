#1-add two numbers

def add(num1,num2):
    sum = num1 + num2
    return sum
num1 = float(input(" NUM1> "))
num2 = float(input(" NUM2> "))
print(add(num1,num2))


#2-Factorilal of number

def Factorilal(number):
    if number < 0:
        print("No Factorial for Negative numbers") 
    elif number == 0:
        print("Factorial of 0 is 1")
    else:
        number > 1
        count  = 1
        for i in range(1,number+1):
            count = count * i
        print(f"Factorial of number is {count}")
number = int(input("enter the number> "))
Factorilal(number)


#3-SimpleIntrest

def SimpleIntrest(P,T,R):
    si = (P * T * R)/100
    print(f"simple intrest is:{si}")
P=int(input("principal amount:> "))
T=int(input("time:> "))
R=int(input("rate:> "))
SimpleIntrest(P,T,R)


#4-CompoundIntrest

def CompoundIntrest(P,R,T):
    ci = P * (pow((1 + R /100),T))
    print(f"Compound intrest is:{ci}")
P=float(input("principal amount:> "))
R=float(input("rate:> "))
T=float(input("time:> "))
CompoundIntrest(P,R,T)


#5-To check amsstrong number

n = int(input("> "))
a = list(map(int,str(n)))
b = list(map(lambda  x:x**3,a))
if sum(b)==n:
    print("The number is an Amstrong",n)
else:
    print("The number is not an Amstrong",n)
    

#6-Area of a circle

def aoc(r):
    PI = 3.142
    return PI * (r * r)
r = int(input("> "))
print("Area of a circle is",aoc(r))


#7-to print prime numbers in an interval

def primenumbers(start,end):
    for value in range(start,end+1):
        if value > 1:
            for i in range(2,value):
                if value % i == 0:
                    break
            else:
                print(value)
start = int(input("> "))
end = int(input("> "))
primenumbers(start,end)


#8-To check prime number or not

def tocheck(number):
    if number > 1:
        for i in range(2,number):
            if number % i == 0:
                print(f"{number} is not a prime a number")
        else:
            print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
number = int(input("> "))
tocheck(number)


#9-nth Fionacci number

def Fibonnaci(number):
    if number < 0:
        print("Incorrect input")
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return Fibonnaci(number-1)+Fibonnaci(number-2)
number = int(input("> "))
print(Fibonnaci(number))


#10-program for Fibonaci numbers

def Fibonnaci(number):
    if number < 0:
        print("Incorrect input")
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return Fibonnaci(number-1)+Fibonnaci(number-2)
number = int(input("> "))
print(Fibonnaci(number))


#11-To check given number is a fibonnaci or not

import math

def isPerfectsquare(x):
    s = int(math.sqrt(x))
    return s*s == x
def isFibonnaci(n):
    return isPerfectsquare(5*n*n+4)
for i in range(1,11):
    if isPerfectsquare(i) == True:
        print(i,"is a fibonnaci number")
    else:
        print(i,"is not a fibonnaci number")


#12-nth multiple of a number in fibonnaci series

def findposition(k,n):
    f1=0
    f2=1
    i=2
    while i!=0:
        f3=f1 + f2
        f1 = f2
        f2 = f3

        if f2 % k ==0:
            return n*i
        i+=1
    return
n = 5
k= 4
print("Position of n\'th multiple of k in""Fibonacci Seires is",findposition(k,n))


#13-ASCII value of a character

def ASCII(s):
    print(f"ASCII value of {s} is",ord(s))
s=str(input("> "))
ASCII(s)


#14-Python Program for Sum of squares of first n natural numbers

def squaresum(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + (i * i)
    return sum
n = int(input("> "))
print(squaresum(n))


#15-Python Program for cube sum of first n natural numbers

def sumOfseries(n):
    sum = 0
    for i in range(1,n+1):
        sum+=i*i*i
    return sum
n=int(input("> "))
print(sumOfseries(n))
