# is_twisted_prime

def is_twisted_prime(n):

    reverse = int(str(n)[::-1])
    max_val = max(n, reverse)

    res = [True] * (max_val + 1)
    res[1] = res[0] = False

    for i in range(2, int(max_val**0.5)+1):
        if res[i]:
            for j in range(i*i, max_val+1, i):
                res[j] = False

    if res[n] and res[reverse]:
        return True
    return False


print(is_twisted_prime(12))
