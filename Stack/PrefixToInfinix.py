#Prefix to Infix

#Read the Prefix expression in reverse order (from right to left)
#If the symbol is an operand, then push it onto the Stack
#If the symbol is an operator, then pop two operands from the Stack 
#Create a string by concatenating the two operands and the operator between them. 
#string = (operand1 + operator + operand2) 
#And push the resultant string back to Stack
#Repeat the above steps until the end of Prefix expression.
#At the end stack will have only 1 string i.e resultant string

# Python Program to convert prefix to Infix
def prefixToInfix(prefix):
	stack = []
	
	# read prefix in reverse order
	i = len(prefix) - 1
	while i >= 0:
		if not isOperator(prefix[i]):
			
			# symbol is operand
			stack.append(prefix[i])
			i -= 1
		else:
		
			# symbol is operator
			str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
			stack.append(str)
			i -= 1
	
	return stack.pop()

def isOperator(c):
	if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
		return True
	else:
		return False

# Driver code
if __name__=="__main__":
	str = "*-A/BC-/AKL"
	print(prefixToInfix(str))

