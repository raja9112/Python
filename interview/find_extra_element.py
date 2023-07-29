def program(a, b):
       
       extra_element= sum(a)-sum(b)
       find= a.index(extra_element)
       print(find)

a=[1,2,3,4,5,6]
b=[1,2,3,4,5]

print(program(a,b))