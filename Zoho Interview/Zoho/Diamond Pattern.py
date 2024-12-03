# Mount blue Coding interview

# 1
# 222
# 33333
# 4444444
# 33333
# 222
# 1

n = 4
s = 1
odd = 1

while s < n+1:
    print(str(s) * odd, end='\n')
    s += 1
    odd += 2

while s != 0:
    s -= 1
    odd -= 2
    temp_odd = odd - 2
    print(str(s-1) * temp_odd, end='\n')