def _z(n):
    s=0
    while n: n//=5;s+=n
    return s

def minimum_factorials_for_zeroes(targets):
    out=[]
    for k in targets:
        lo,hi=0,5*k
        while lo<hi:
            mid=(lo+hi)//2
            if _z(mid)>=k: hi=mid
            else: lo=mid+1
        out.append(lo)
    return out
