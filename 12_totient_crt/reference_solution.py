from math import gcd

def _egcd(a,b):
    if b==0:return a,1,0
    g,x,y=_egcd(b,a%b); return g,y,x-(a//b)*y

def _phi(n):
    r=n;p=2;x=n
    while p*p<=x:
        if x%p==0:
            while x%p==0:x//=p
            r-=r//p
        p+=1
    if x>1:r-=r//x
    return r

def solve_congruence_system(congruences):
    a,m=0,1
    for b,n in congruences:
        b%=n; g,x,_=_egcd(m,n); diff=b-a
        if diff%g:return None
        step=(diff//g*x)%(n//g); l=m//g*n; a=(a+m*step)%l; m=l
    return a,m,_phi(m)
