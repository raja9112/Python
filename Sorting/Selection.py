input_user=int(input("How many number you want to enter : "))
#sort_num=[ int(input(f"Enter {input_user} numbers : ")) for i in range(input_user)]
sort_num=[]
for i in range(input_user):
    sort_num.append(int(input(f"enter {input_user} numbers :")))

print("Unsorted array: ", sort_num)

for j in range(len(sort_num) - 1):
    m_val= min(sort_num[j:])
    m_ind= sort_num.index(m_val, j) # j is for sorting duplicates values
    
    if sort_num[j] != sort_num[m_ind]:
        sort_num[j], sort_num[m_ind]= sort_num[m_ind], sort_num[j]
       
    print(sort_num)

print("Sorted array: ", sort_num)