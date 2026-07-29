def prime_count_queries(ranges):
    if not ranges:return []
    m=max(r for _,r in ranges); prime=bytearray(b'\x01')*(m+1)
    if m>=0: prime[0]=0
    if m>=1: prime[1]=0
    p=2
    while p*p<=m:
        if prime[p]: prime[p*p:m+1:p]=b'\x00'*(((m-p*p)//p)+1)
        p+=1
    pref=[0]*(m+1); run=0
    for i,v in enumerate(prime): run+=v; pref[i]=run
    return [pref[r]-(pref[l-1] if l else 0) for l,r in ranges]
