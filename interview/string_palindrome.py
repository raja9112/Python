def palindrome(s):
    rev= "".join(reversed(s))
    if (s==rev):                                              #s== s[::-1]
        print(f"The {s} string is palindrome.")
    else:
        print(f"The {s} string is not a palindrome.")

user=input("Enter a string to check :")
print(f"The given string: {user}")
palindrome(user)