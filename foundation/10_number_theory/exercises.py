"""10 — Number theory.
Topics: primes, factors, sieves, modular arithmetic, coprimality, and Diophantine reasoning.
"""


def is_prime(n:int)->bool: raise NotImplementedError

def prime_factors(n:int)->list[int]: raise NotImplementedError

def divisors(n:int)->list[int]: raise NotImplementedError

def divisor_count(n:int)->int: raise NotImplementedError

def sieve(limit:int)->list[int]: raise NotImplementedError

def are_coprime(a:int,b:int)->bool: raise NotImplementedError

def euler_totient(n:int)->int: raise NotImplementedError

def modular_inverse(a:int,m:int)->int|None: raise NotImplementedError

def chinese_remainder_pair(a1:int,m1:int,a2:int,m2:int)->int|None: raise NotImplementedError

def count_trailing_zeros_factorial(n:int)->int: raise NotImplementedError

TESTS=[
("is_prime",(97,),True),("prime_factors",(84,),[2,2,3,7]),
("divisors",(12,),[1,2,3,4,6,12]),("divisor_count",(36,),9),
("sieve",(10,),[2,3,5,7]),("are_coprime",(14,25),True),
("euler_totient",(9,),6),("modular_inverse",(3,11),4),
("chinese_remainder_pair",(2,3,3,5),8),("count_trailing_zeros_factorial",(100,),24)]

def main():
 print("\nSample tests\n"+"-"*50)
 for n,a,e in TESTS[:2]:
  r=globals()[n](*a); assert r==e,f"{n}: expected {e}, got {r}"; print(f"[PASS] {n}")
 print("\nSample tests passed. Running all tests...\n\nFull test suite\n"+"-"*50)
 for n,a,e in TESTS:
  r=globals()[n](*a); assert r==e,f"{n}: expected {e}, got {r}"; print(f"[PASS] {n}")
 print(f"\nOK — {len(TESTS)} questions passed")
if __name__=="__main__": main()
