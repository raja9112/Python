def balanced_brackets(expr):
    stack=[]

    for char in expr:
        if char in ["(","[","{"]:
            stack.append(char)
        else:
            
            current=stack.pop()
            if current== '(':
                if char != ')':
                    return False
            if current== '[':
                if char != ']':
                    return False
            if current== '{':
                if char != '}':
                    return False
    if stack:
        return False
    return True

expr="{()}[]"
if balanced_brackets(expr):
    print("Balanced")
else:
    print("Not balanced")