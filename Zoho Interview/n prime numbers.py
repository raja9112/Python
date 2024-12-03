# Print n prime numbers

def is_prime(n):
    # if n < 2:
    #     return False
    
    # for i in range(0, int(n**0.5)+ 1):
    #     if n%1 == 0:
    #         return False
    # return True

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5)+1):   
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False

    return [x for x in range(n + 1) if is_prime[x]]

print(is_prime(12))


# Time: O(nlog(log(n)))
# Space: (n)