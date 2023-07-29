#Insertion sorting algorithm

def insertionsort(my_list):
    for i in range(1, len(my_list)):
        current_element= my_list[i]
        pos=i
        while (current_element<my_list[pos - 1] and pos>0):
            my_list[pos]= my_list[pos - 1]
            pos-=1
        my_list[pos]= current_element
        print(my_list)   #prints full steps
    print()   #it will give a  gap 
    #print(my_list)  prints answer
list1=[2,4,9,1,6]
insertionsort(list1)
print(list1)