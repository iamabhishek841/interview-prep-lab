from math import isqrt

def _prime(n):
    if n<2:return False
    if n==2:return True
    if n%2==0:return False
    return all(n%d for d in range(3,isqrt(n)+1,2))

def is_two_sided_truncatable_prime(n):
    s=str(n)
    if n<=0 or '0' in s:return False
    return all(_prime(int(s[i:])) for i in range(len(s))) and all(_prime(int(s[:i])) for i in range(len(s),0,-1))
