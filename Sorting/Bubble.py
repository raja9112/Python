class Bubble():
    def example(self, input_user):
        # input_user=int(input("How many number you want to enter : "))
        #sort_num=[ int(input(f"Enter {input_user} numbers : ")) for i in range(input_user)]
        sort_num=[]
        for i in range(input_user):
            sort_num.append(int(input(f"enter {input_user} numbers :")))

        n=len(sort_num)
        for j in range(n):
            for k in range(n - 1 - j):
                if sort_num[k] > sort_num[k+1]:
                    sort_num[k], sort_num[k+1] = sort_num[k+1], sort_num[k]
                    print(sort_num)

                else:
                    print(sort_num)
            print()
obj=Bubble()
x=int(input("How many number you want to enter : "))
obj.example(x)