def shellsort(my_list):
    gap=len(my_list)//2
    while gap>0:
        for i in range(gap, len(my_list)):
            current_element=my_list[i]
            pos=i
            while(current_element<my_list[pos-gap] and pos>=gap):
                my_list[pos]= my_list[pos-gap]
                pos-=gap
            my_list[pos]= current_element
        gap=gap//2


num= int(input("Enter length of list: "))
list1=[int(input()) for x in range(num)]
print(f"Unsorted list {list1}")
shellsort(list1)
print(f"Sorted list: {list1}")