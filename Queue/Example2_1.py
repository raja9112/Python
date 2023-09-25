#Using put(item, block=True, timeout=none)
#put_nowait(item)
#get(item, block=True, timeout=None)
#get_nowait()

import queue
q=queue.PriorityQueue(maxsize=5)
def adding():
    try:
        x=input("Enter the element: ")
        q.put_nowait(x)
        print(f'The added element is {x}')
        print(q)
    except:
        print("The Queue is full")

def removing():
    try:
        y=q.get_nowait()
        print(f'The removed element is {y}')
        print(q)
    except:
        print("The Queue is Empty")

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