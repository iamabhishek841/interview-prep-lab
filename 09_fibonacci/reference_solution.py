def _pair(n,m):
    if n==0:return 0,1%m
    a,b=_pair(n//2,m); c=a*((2*b-a)%m)%m; d=(a*a+b*b)%m
    return (d,(c+d)%m) if n&1 else (c,d)

def fibonacci_mod_queries(queries): return [_pair(n,m)[0] for n,m in queries]
