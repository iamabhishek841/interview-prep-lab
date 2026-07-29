def combination_queries(queries,modulus):
    if not queries:return []
    m=max(n for n,_ in queries); fact=[1]*(m+1)
    for i in range(1,m+1):fact[i]=fact[i-1]*i%modulus
    inv=[1]*(m+1); inv[m]=pow(fact[m],modulus-2,modulus)
    for i in range(m,0,-1):inv[i-1]=inv[i]*i%modulus
    return [0 if r<0 or r>n else fact[n]*inv[r]%modulus*inv[n-r]%modulus for n,r in queries]
