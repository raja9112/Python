"""Postfix: An expression is called the postfix expression if the operator appears in the expression after the operands. Simply of the form (operand1 operand2 operator). 
Example : AB+CD-* (Infix : (A+B) * (C-D) )

Prefix : An expression is called the prefix expression if the operator appears in the expression before the operands. Simply of the form (operator operand1 operand2). 
Example : *+AB-CD (Infix : (A+B) * (C-D) )"""

"""Input :  Postfix : AB+CD-*
Output : Prefix :  *+AB-CD
Explanation : Postfix to Infix : (A+B) * (C-D)
              Infix to Prefix :  *+AB-CD      """

"""Read the Postfix expression from left to right
If the symbol is an operand, then push it onto the Stack
If the symbol is an operator, then pop two operands from the Stack 
Create a string by concatenating the two operands and the operator before them. 
string = operator + operand2 + operand1 
And push the resultant string back to Stack
Repeat the above steps until end of Postfix expression."""

s="AB+CD-*"
stack=[]

operators={'+', '-', '*', '/', '^'}

for i in s:
    if i in operators:
        a=stack.pop()
        b=stack.pop()
        #temp=i+a+b     ['*-DC+BA']
        temp=i+b+a
        stack.append(temp)
    
    else:
        stack.append(i)

print(stack)