def palindrome(num):
    if str(num)==str(num)[::-1]:
        print("the number is palindrome.")
    else:
        print("the number is not a palindrome")

user= int(input("Enter a number :"))
palindrome(user)