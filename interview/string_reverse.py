#Reversal of a string using recursion 
def Recursion_reversal(n):
    if len(n) == 0:
        return n
    else:
        return Recursion_reversal(n[1:])+n[0]

print(Recursion_reversal(input("Enter a word: ")))