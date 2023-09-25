#Example program for Queue implementation

import collections

q=collections.deque()
def adding():
    x=input("Enter the element: ")
    q.append(x)
    print(f'The added element is {x}')
    print(q)

def removing():
    y=q.popleft()
    print(f'The removed element is {y}')
    print(q)

while True:
    print("""Enter the choice
    1. Add
    2. Remove
    3. Stop""")
    choice=int(input("Enter the choice: "))

    if choice == 1:
        adding()
    elif choice == 2:
        removing()
    elif choice == 3:
        break
    else:
        print("Invalid choice")