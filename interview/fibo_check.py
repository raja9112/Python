#Fibonacci series of numbers is a series of numbers formed by the addition of the preceding two numbers.
from cmath import sqrt
import math

def perfectnumber(n):
    s= int(math.sqrt(n))
    return s*s==n           #return true if the n is perfect number

def check_fibo(x):
    return perfectnumber(5*x*x+4) or perfectnumber(5*x*x-4)

#for i in range(1, 11):
#    if (check_fibo(i)==True):
#        print(f"{i} is a fibonacci number")
#    else:
#        print(f"{i} is not a fibonacci number")

n=int(input("which number do you want to check : "))
if (check_fibo(n)==True):
    print(f"{n} is a fibonacci number.")
else:
    print(f"{n} is not a fibonacci number.")