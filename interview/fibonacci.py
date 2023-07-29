#from geeks for geeks
#fibonacci is like adding numbers for example 0+1=2, now 1+2= 3.... etc
#fibonacci numbers 0,1,1,2,3,5,8,13,21,34, etc...
#Fibonacci series of numbers is a series of numbers formed by the addition of the preceding two numbers.
def fibonacci(n):

    if (n<0):
        return "incorrect input"
    elif (n==0):
        return 0
    elif (n==1 or n==2):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
#driver code
num=int(input("enter a number:"))
print(fibonacci(num))
