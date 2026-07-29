def factor_profile(n):
    x=n; factors=[]; p=2
    while p*p<=x:
        if x%p==0:
            e=0
            while x%p==0:x//=p;e+=1
            factors.append((p,e))
        p=3 if p==2 else p+2
    if x>1:factors.append((x,1))
    divs=[1]
    for p,e in factors:
        old=divs[:]; power=1
        for _ in range(e):
            power*=p; divs += [d*power for d in old]
    divs.sort()
    return {'factors':factors,'divisors':divs,'count':len(divs),'sum':sum(divs)}
