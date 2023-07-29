#selection sort without using min or max keyword

input_user=int(input("How many number you want to enter : "))
#sort_num=[ int(input(f"Enter {input_user} numbers : ")) for i in range(input_user)]
sort_num=[]
for i in range(input_user):
    sort_num.append(int(input(f"enter {input_user} numbers :")))

print("Unsorted array : ", sort_num)

for j in range(len(sort_num) - 1):
    m_val= sort_num[j]

    for x in range(j+1, len(sort_num)):
        if sort_num[x]< m_val:
            m_val= sort_num[x]

    m_ind= sort_num.index(m_val, j)
    if sort_num[j] != sort_num[m_ind]:
        sort_num[j], sort_num[m_ind]= sort_num[m_ind], sort_num[j]
    print(sort_num)

print("Sorted list: ", sort_num)