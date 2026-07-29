from math import gcd

def count_divisible_queries(queries):
    out=[]
    for left,right,a,b in queries:
        lcm=(a//gcd(a,b))*b
        def upto(x,d): return 0 if x<0 else x//d
        def interval(d): return upto(right,d)-upto(left-1,d)
        out.append(interval(a)+interval(b)-interval(lcm))
    return out
