#1. queue modules
import queue
stack= queue.LifoQueue()  #LifoQueue() is not iterable, so we cannot use for loop 

while True:
    choice=int(input("Choice (1.add, 2.pop, 3.quit):  "))
    if choice==1:
        add=int(input("Enter the element: "))
        stack.put(add)
        print(stack)

    elif choice==2:
        remove=stack.get()
        print(f"Removed element is {remove}")
        print(stack)

    elif choice==3:
        break

    else:
        print("Invalid choice")