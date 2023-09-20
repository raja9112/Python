#Basic example for stack
#Implementing stack using list

stack=[]

def push():
    if len(stack)==n:
        print("You have attained the limit")
    else:
        element=int(input("Enter the element:"))
        stack.append(element)
        print(stack)

def pop_element():
    if not stack:
        print("Stack is empty")

    else:
        r=stack.pop()
        print(f"The removed item is{r}")
        print(stack)

n=int(input("Enter the limit for stack: "))
while True:
    print("""Select your choice:
                1. Push
                2. Pop
                3. Quit""")

    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("Invalid choice")