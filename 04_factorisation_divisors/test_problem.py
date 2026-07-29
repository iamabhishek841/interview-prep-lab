from problem import factor_profile as f

def test_one(): assert f(1)=={'factors':[],'divisors':[1],'count':1,'sum':1}
def test_prime(): assert f(13)=={'factors':[(13,1)],'divisors':[1,13],'count':2,'sum':14}
def test_twelve(): assert f(12)=={'factors':[(2,2),(3,1)],'divisors':[1,2,3,4,6,12],'count':6,'sum':28}
def test_prime_power(): assert f(32)['count']==6
def test_square(): assert f(36)['divisors']==[1,2,3,4,6,9,12,18,36]
def test_distinct_primes(): assert f(30)['count']==8
def test_sum_perfect_number(): assert f(28)['sum']==56
def test_large_prime(): assert f(999983)['factors']==[(999983,1)]
def test_semiprime(): assert f(1009*1013)['factors']==[(1009,1),(1013,1)]
def test_sorted():
 d=f(360)['divisors']; assert d==sorted(d) and len(d)==24
def test_product_reconstructs():
 r=f(7560); x=1
 for p,e in r['factors']: x*=p**e
 assert x==7560
