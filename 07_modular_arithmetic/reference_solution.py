def _egcd(a,b):
    x0,x1=1,0
    while b: q,a,b=a//b,b,a%b; x0,x1=x1,x0-q*x1
    return a,x0

def modular_division_queries(queries):
    out=[]
    for n,d,m in queries:
        g,x=_egcd(d%m,m)
        out.append(None if g!=1 else (n%m)*(x%m)%m)
    return out
