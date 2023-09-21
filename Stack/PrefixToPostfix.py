#Prefix to Postfix

#1st prefix to infix and then infix to postfix

#Input :  Prefix :  *+AB-CD
#Output : Postfix : AB+CD-*
#Explanation : Prefix to Infix :  (A+B) * (C-D)
#              Infix to Postfix :  AB+CD-*

"""Read the Prefix expression in reverse order (from right to left)
If the symbol is an operand, then push it onto the Stack
If the symbol is an operator, then pop two operands from the Stack 
Create a string by concatenating the two operands and the operator after them. 
string = operand1 + operand2 + operator 
And push the resultant string back to Stack
Repeat the above steps until end of Prefix expression."""

s="*+AB-CD"

stack=[]

s=s[::-1]

operators={'+', '-', '*', '/', '^'}

for i in s:
    if i in operators:
        a=stack.pop()
        b=stack.pop()
        temp=a+b+i
        stack.append(temp)

    else:
        stack.append(i)

print(stack.pop())

"""Time Complexity: O(N), as we are using a loop for traversing the expression.

Auxiliary Space: O(N), as we are using stack for extra space.
"""
