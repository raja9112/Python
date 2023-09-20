#1. Collection modules
import collections
stack= collections.deque()

while True:
    choice=int(input("Choice (1.add, 2.pop, 3.quit):  "))
    if choice==1:
        add=int(input("Enter the element: "))
        stack.append(add)
        print(stack)

    elif choice==2:
        remove=stack.pop()
        print(f"Removed element is {remove}")
        print(stack)

    elif choice==3:
        break

    else:
        print("Invalid choice")