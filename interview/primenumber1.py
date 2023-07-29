def check_prime(num):

    n=int(num/2)+1     #5
    if num>1:
        for i in range(2, n):       #iterate take place from 2 to 4  (n=5)
            if (num%i)==0:          #so the num(4) is divide by 2,3,4 and if gets remainder zero means it is not a prime number 
                print(f"{num} It is not a prime number.")
                break
        else:
            print(f"{num} is a prime number.")
    else:
        print(f"{num} is a not a prime number")

user=int(input("Enter a number: "))
check_prime(user)