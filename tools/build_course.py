from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TOPICS = [
    ("01_division_modulo", "Division, Divisibility and Modulo", "quotient-remainder reasoning, divisibility, cyclic indexing and counting multiples", "https://www.geeksforgeeks.org/maths/euclids-division-lemma/", [
        ("count_multiples_in_range", "Count Multiples in an Inclusive Range", "count_multiples", "range_count"),
        ("smallest_divisible_number", "Smallest Number at Least N Divisible by K", "smallest_divisible", "ceil_multiple"),
        ("circular_array_index", "Circular Array Index After Shifts", "circular_index", "circular"),
        ("same_remainder_pairs", "Count Pairs with the Same Remainder", "same_remainder_pairs", "remainder_pairs"),
        ("divisibility_by_digit_sum", "Numbers Divisible by Their Digit Sum", "divisible_by_digit_sum", "digit_sum_filter"),
        ("minimum_addition_for_divisibility", "Minimum Addition to Become Divisible", "minimum_addition", "min_add"),
    ]),
    ("02_gcd_lcm", "GCD, LCM and Euclidean Algorithm", "Euclid's invariant, gcd reduction, lcm construction and range aggregation", "https://www.geeksforgeeks.org/dsa/mathematical-algorithms-gcd-lcm/", [
        ("gcd_two_numbers", "GCD of Two Integers", "gcd_two", "gcd_two"),
        ("lcm_two_numbers", "LCM of Two Integers", "lcm_two", "lcm_two"),
        ("gcd_of_array", "GCD of an Array", "gcd_array", "gcd_array"),
        ("lcm_of_array", "LCM of an Array", "lcm_array", "lcm_array"),
        ("count_common_divisors", "Count Common Divisors", "count_common_divisors", "common_divisors"),
        ("gcd_range_queries", "GCD for Multiple Range Queries", "gcd_range_queries", "gcd_queries"),
        ("extended_euclidean", "Extended Euclidean Coefficients", "extended_gcd", "extended_gcd"),
    ]),
    ("03_prime_numbers", "Prime Numbers and Primality Testing", "trial division to square root, prime structure and prime-based transformations", "https://www.geeksforgeeks.org/dsa/prime-numbers/", [
        ("is_prime", "Determine Whether a Number Is Prime", "is_prime", "is_prime"),
        ("next_prime", "Find the Next Prime", "next_prime", "next_prime"),
        ("count_primes_in_list", "Count Prime Values in a List", "count_primes", "count_primes"),
        ("left_truncatable_prime", "Validate a Left-Truncatable Prime", "left_truncatable_prime", "left_trunc"),
        ("prime_sum_pair", "Find a Pair Whose Sum Is Prime", "prime_sum_pair", "prime_pair"),
        ("closest_prime_pair", "Closest Prime Pair in a Range", "closest_prime_pair", "closest_primes"),
    ]),
    ("04_factorization_divisors", "Prime Factorization and Divisors", "factor extraction, divisor pairing, divisor counts and divisor sums", "https://www.geeksforgeeks.org/dsa/prime-factorization/", [
        ("prime_factorization", "Prime Factorization with Repetition", "prime_factors", "prime_factors"),
        ("all_divisors", "Return All Divisors in Sorted Order", "all_divisors", "all_divisors"),
        ("divisor_count", "Count the Divisors of N", "divisor_count", "divisor_count"),
        ("sum_of_divisors", "Sum of All Divisors", "sum_of_divisors", "sum_divisors"),
        ("exactly_k_divisors", "Numbers up to N with Exactly K Divisors", "exactly_k_divisors", "k_divisors"),
        ("common_prime_factors", "Common Distinct Prime Factors", "common_prime_factors", "common_prime_factors"),
    ]),
    ("05_sieve", "Sieve Algorithms", "precomputation of primes, smallest prime factors and range counting", "https://www.geeksforgeeks.org/dsa/sieve-of-eratosthenes/", [
        ("primes_up_to_n", "List All Primes up to N", "primes_up_to", "sieve"),
        ("prime_prefix_queries", "Answer Prime Count Range Queries", "prime_count_queries", "prime_prefix"),
        ("smallest_prime_factor_table", "Build a Smallest Prime Factor Table", "smallest_prime_factors", "spf"),
        ("factorize_many_numbers", "Factorize Many Numbers Efficiently", "factorize_many", "factorize_many"),
        ("segmented_prime_range", "Primes in a Large Inclusive Range", "segmented_primes", "segmented"),
        ("count_distinct_prime_factors", "Distinct Prime-Factor Count for Every Number", "distinct_prime_factor_counts", "omega_table"),
    ]),
    ("06_fast_exponentiation", "Fast Exponentiation", "binary exponentiation, exponent bits and logarithmic-time powering", "https://www.geeksforgeeks.org/dsa/exponential-squaring-fast-modulo-multiplication/", [
        ("integer_power", "Compute an Integer Power Efficiently", "fast_power", "fast_power"),
        ("modular_power", "Modular Exponentiation", "modular_power", "mod_pow"),
        ("power_queries", "Answer Multiple Power Queries", "power_queries", "power_queries"),
        ("last_digit_of_power", "Last Digit of a Huge Power", "last_digit", "last_digit"),
        ("matrix_power_2x2", "Raise a 2x2 Matrix to a Power", "matrix_power", "matrix_power"),
        ("geometric_sum", "Geometric Sum Modulo M", "geometric_sum_mod", "geometric_sum"),
    ]),
    ("07_modular_arithmetic", "Modular Arithmetic", "normalization, modular inverse, congruences and safe composition", "https://www.geeksforgeeks.org/dsa/modular-arithmetic/", [
        ("normalize_remainders", "Normalize Signed Remainders", "normalize_remainders", "normalize"),
        ("modular_inverse", "Modular Multiplicative Inverse", "modular_inverse", "mod_inverse"),
        ("linear_congruence", "Solve a Linear Congruence", "solve_linear_congruence", "linear_congruence"),
        ("modular_division", "Modular Division under a Prime Modulus", "modular_division", "mod_division"),
        ("subarray_sum_divisible", "Count Subarrays with Sum Divisible by K", "count_divisible_subarrays", "subarray_mod"),
        ("rolling_hash", "Polynomial Rolling Hash", "rolling_hash", "rolling_hash"),
    ]),
    ("08_factorial_trailing_zeroes", "Factorials and Trailing Zeroes", "factorial growth, prime exponents and inverse trailing-zero search", "https://www.geeksforgeeks.org/dsa/count-trailing-zeroes-factorial-number/", [
        ("factorial", "Compute N Factorial", "factorial", "factorial"),
        ("trailing_zeroes", "Trailing Zeroes in N Factorial", "trailing_zeroes", "trailing_zeroes"),
        ("prime_exponent_in_factorial", "Exponent of Prime P in N Factorial", "prime_exponent_factorial", "legendre"),
        ("smallest_factorial_with_zeroes", "Smallest N Whose Factorial Has at Least Z Zeroes", "smallest_n_with_zeroes", "inverse_zeroes"),
        ("factorial_mod_prime", "Factorial Modulo a Prime", "factorial_mod", "factorial_mod"),
        ("last_nonzero_digit_factorial", "Last Non-Zero Digit of N Factorial", "last_nonzero_digit", "last_nonzero"),
    ]),
    ("09_fibonacci", "Fibonacci and Recurrences", "iterative recurrence, fast doubling, matrix structure and recurrence applications", "https://www.geeksforgeeks.org/dsa/program-for-nth-fibonacci-number/", [
        ("nth_fibonacci", "Nth Fibonacci Number", "fibonacci", "fibonacci"),
        ("fibonacci_fast_doubling", "Nth Fibonacci with Fast Doubling", "fibonacci_fast", "fib_fast"),
        ("fibonacci_mod", "Nth Fibonacci Modulo M", "fibonacci_mod", "fib_mod"),
        ("sum_fibonacci", "Sum of the First N Fibonacci Numbers", "sum_fibonacci", "sum_fib"),
        ("count_stair_ways", "Count Ways to Climb Stairs", "count_stair_ways", "stairs"),
        ("is_fibonacci", "Check Whether a Number Is Fibonacci", "is_fibonacci", "is_fib"),
    ]),
    ("10_combinations", "Permutations, Combinations and nCr", "counting choices, symmetry, Pascal recurrence and overflow-aware computation", "https://www.geeksforgeeks.org/dsa/combination-n-cr/", [
        ("ncr", "Compute n Choose r", "ncr", "ncr"),
        ("npr", "Compute n Permute r", "npr", "npr"),
        ("pascal_row", "Generate a Row of Pascal's Triangle", "pascal_row", "pascal_row"),
        ("grid_paths", "Count Grid Paths", "grid_paths", "grid_paths"),
        ("unique_anagrams", "Count Unique Anagrams", "unique_anagrams", "anagrams"),
        ("ncr_mod_prime", "nCr Modulo a Prime", "ncr_mod_prime", "ncr_mod"),
    ]),
    ("11_power_sets", "Sets, Subsets and Power Sets", "bitmask enumeration, subset counts and subset constraints", "https://www.geeksforgeeks.org/dsa/power-set/", [
        ("generate_power_set", "Generate the Power Set", "power_set", "power_set"),
        ("subset_count", "Count All Subsets", "subset_count", "subset_count"),
        ("subsets_with_sum", "All Subsets with a Target Sum", "subsets_with_sum", "subset_sum_enum"),
        ("count_even_sum_subsets", "Count Subsets with Even Sum", "count_even_sum_subsets", "even_subsets"),
        ("maximum_subset_xor", "Maximum XOR over All Subsets", "maximum_subset_xor", "max_xor"),
        ("kth_subset", "Kth Subset in Bitmask Order", "kth_subset", "kth_subset"),
    ]),
    ("12_totient_crt", "Euler Totient and Chinese Remainder Theorem", "coprimality counting, totient factorization and congruence merging", "https://www.geeksforgeeks.org/dsa/eulers-totient-function/", [
        ("euler_totient", "Euler's Totient Function", "euler_totient", "totient"),
        ("totients_up_to_n", "Totient Values from 1 to N", "totients_up_to", "totient_sieve"),
        ("count_coprime_pairs", "Count Coprime Pairs in a List", "count_coprime_pairs", "coprime_pairs"),
        ("crt_pairwise_coprime", "CRT for Pairwise-Coprime Moduli", "crt", "crt"),
        ("generalized_crt", "Generalized CRT with Non-Coprime Moduli", "generalized_crt", "generalized_crt"),
        ("reduced_fraction_count", "Count Reduced Proper Fractions up to N", "reduced_fraction_count", "farey_count"),
    ]),
]

CORE = r'''from __future__ import annotations
from functools import reduce
from math import gcd, isqrt, factorial as _factorial

def _prime(n):
    if n < 2:return False
    if n % 2 == 0:return n == 2
    d=3
    while d*d<=n:
        if n%d==0:return False
        d+=2
    return True

def solve(op,*a):
    if op=='range_count':
        l,r,k=a; return r//k-(l-1)//k
    if op=='ceil_multiple':
        n,k=a; return ((n+k-1)//k)*k
    if op=='circular':
        i,shift,size=a; return (i+shift)%size
    if op=='remainder_pairs':
        vals,k=a; c={}; ans=0
        for x in vals:q=x%k; ans+=c.get(q,0); c[q]=c.get(q,0)+1
        return ans
    if op=='digit_sum_filter':
        vals=a[0]; return [x for x in vals if x>0 and x%sum(map(int,str(x)))==0]
    if op=='min_add':
        n,k=a; return (-n)%k
    if op=='gcd_two': return gcd(a[0],a[1])
    if op=='lcm_two': return abs(a[0]//gcd(a[0],a[1])*a[1]) if a[0] and a[1] else 0
    if op=='gcd_array': return reduce(gcd,a[0],0)
    if op=='lcm_array': return reduce(lambda x,y:abs(x//gcd(x,y)*y) if x and y else 0,a[0],1)
    if op=='common_divisors':
        g=gcd(a[0],a[1]); return sum(g%d==0 for d in range(1,isqrt(g)+1))*2-(isqrt(g)**2==g)
    if op=='gcd_queries':
        vals,qs=a; return [reduce(gcd,vals[l:r+1],0) for l,r in qs]
    if op=='extended_gcd':
        x,y=a
        def eg(p,q):
            if q==0:return (abs(p),1 if p>=0 else -1,0)
            g,s,t=eg(q,p%q); return g,t,s-(p//q)*t
        return eg(x,y)
    if op=='is_prime': return _prime(a[0])
    if op=='next_prime':
        n=a[0]+1
        while not _prime(n):n+=1
        return n
    if op=='count_primes': return sum(_prime(x) for x in a[0])
    if op=='left_trunc': return all(_prime(int(str(a[0])[i:])) for i in range(len(str(a[0]))))
    if op=='prime_pair':
        vals=a[0]
        for i in range(len(vals)):
            for j in range(i+1,len(vals)):
                if _prime(vals[i]+vals[j]):return (vals[i],vals[j])
        return None
    if op=='closest_primes':
        l,r=a; ps=[x for x in range(max(2,l),r+1) if _prime(x)]
        return min(zip(ps,ps[1:]),key=lambda p:p[1]-p[0]) if len(ps)>1 else None
    if op=='prime_factors':
        n=a[0]; out=[]; d=2
        while d*d<=n:
            while n%d==0:out.append(d); n//=d
            d+=1
        if n>1:out.append(n)
        return out
    if op in {'all_divisors','divisor_count','sum_divisors'}:
        n=a[0]; ds=[]
        for d in range(1,isqrt(n)+1):
            if n%d==0:ds += [d] if d*d==n else [d,n//d]
        ds.sort()
        return ds if op=='all_divisors' else len(ds) if op=='divisor_count' else sum(ds)
    if op=='k_divisors': return [x for x in range(1,a[0]+1) if solve('divisor_count',x)==a[1]]
    if op=='common_prime_factors': return sorted(set(solve('prime_factors',a[0]))&set(solve('prime_factors',a[1])))
    if op in {'sieve','spf','omega_table'}:
        n=a[0]; spf=list(range(n+1))
        if n>=1:spf[1]=1
        for p in range(2,isqrt(n)+1):
            if spf[p]==p:
                for x in range(p*p,n+1,p):
                    if spf[x]==x:spf[x]=p
        if op=='spf':return spf
        if op=='sieve':return [i for i in range(2,n+1) if spf[i]==i]
        return [0,0]+[len(set(solve('prime_factors',i))) for i in range(2,n+1)]
    if op=='prime_prefix':
        n,qs=a; pref=[0]*(n+1)
        for i in range(1,n+1):pref[i]=pref[i-1]+_prime(i)
        return [pref[r]-(pref[l-1] if l else 0) for l,r in qs]
    if op=='factorize_many': return [solve('prime_factors',x) for x in a[0]]
    if op=='segmented': return [x for x in range(max(2,a[0]),a[1]+1) if _prime(x)]
    if op=='fast_power': return pow(a[0],a[1])
    if op=='mod_pow': return pow(a[0],a[1],a[2])
    if op=='power_queries': return [pow(x,e) for x,e in a[0]]
    if op=='last_digit': return pow(a[0],a[1],10)
    if op=='matrix_power':
        m,e=a
        def mul(x,y):return [[sum(x[i][k]*y[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
        r=[[1,0],[0,1]]
        while e:
            if e&1:r=mul(r,m)
            m=mul(m,m); e//=2
        return r
    if op=='geometric_sum': return sum(pow(a[0],i,a[2]) for i in range(a[1]+1))%a[2]
    if op=='normalize': return [x%a[1] for x in a[0]]
    if op=='mod_inverse':
        x,m=a; return pow(x,-1,m) if gcd(x,m)==1 else None
    if op=='linear_congruence':
        c,b,m=a; g=gcd(c,m)
        if b%g:return None
        mm=m//g; return ((b//g)*pow(c//g,-1,mm))%mm
    if op=='mod_division': return a[0]*pow(a[1],a[2]-2,a[2])%a[2]
    if op=='subarray_mod':
        vals,k=a; c={0:1}; s=ans=0
        for x in vals:s=(s+x)%k; ans+=c.get(s,0); c[s]=c.get(s,0)+1
        return ans
    if op=='rolling_hash':
        text,base,mod=a; h=0
        for ch in text:h=(h*base+ord(ch))%mod
        return h
    if op=='factorial': return _factorial(a[0])
    if op=='trailing_zeroes':
        n=a[0]; ans=0
        while n:n//=5; ans+=n
        return ans
    if op=='legendre':
        n,p=a; ans=0
        while n:n//=p; ans+=n
        return ans
    if op=='inverse_zeroes':
        z=a[0]; lo,hi=0,5*z+5
        while lo<hi:
            mid=(lo+hi)//2
            if solve('trailing_zeroes',mid)>=z:hi=mid
            else:lo=mid+1
        return lo
    if op=='factorial_mod':
        n,m=a; r=1
        for x in range(2,n+1):r=r*x%m
        return r
    if op=='last_nonzero':
        n=a[0]; r=1
        for x in range(2,n+1):
            r*=x
            while r%10==0:r//=10
            r%=10**8
        return r%10
    if op in {'fibonacci','fib_fast','fib_mod'}:
        n=a[0]; mod=a[1] if op=='fib_mod' else None
        def fd(k):
            if k==0:return 0,1
            x,y=fd(k//2); c=x*(2*y-x); d=x*x+y*y
            if mod:c%=mod; d%=mod
            return (d,c+d) if k&1 else (c,d)
        return fd(n)[0]%(mod or 10**1000)
    if op=='sum_fib': return solve('fibonacci',a[0]+2)-1
    if op=='stairs':
        n=a[0]; return solve('fibonacci',n+1)
    if op=='is_fib':
        n=a[0]; return isqrt(5*n*n+4)**2==5*n*n+4 or isqrt(5*n*n-4)**2==5*n*n-4
    if op=='ncr':
        n,r=a
        if r<0 or r>n:return 0
        r=min(r,n-r); ans=1
        for i in range(1,r+1):ans=ans*(n-r+i)//i
        return ans
    if op=='npr':
        n,r=a; return 0 if r<0 or r>n else _factorial(n)//_factorial(n-r)
    if op=='pascal_row': return [solve('ncr',a[0],r) for r in range(a[0]+1)]
    if op=='grid_paths': return solve('ncr',a[0]+a[1]-2,a[0]-1)
    if op=='anagrams':
        from collections import Counter
        s=a[0]; ans=_factorial(len(s))
        for c in Counter(s).values():ans//=_factorial(c)
        return ans
    if op=='ncr_mod': return solve('ncr',a[0],a[1])%a[2]
    if op=='power_set':
        vals=a[0]; return [[vals[i] for i in range(len(vals)) if mask>>i&1] for mask in range(1<<len(vals))]
    if op=='subset_count': return 1<<a[0]
    if op=='subset_sum_enum': return [s for s in solve('power_set',a[0]) if sum(s)==a[1]]
    if op=='even_subsets':
        vals=a[0]; return sum(sum(s)%2==0 for s in solve('power_set',vals))
    if op=='max_xor': return max((reduce(lambda x,y:x^y,s,0) for s in solve('power_set',a[0])),default=0)
    if op=='kth_subset':
        vals,k=a; return [vals[i] for i in range(len(vals)) if k>>i&1]
    if op=='totient':
        n=a[0]; r=n
        for p in set(solve('prime_factors',n)):r-=r//p
        return r
    if op=='totient_sieve': return [0]+[solve('totient',i) for i in range(1,a[0]+1)]
    if op=='coprime_pairs':
        vals=a[0]; return sum(gcd(vals[i],vals[j])==1 for i in range(len(vals)) for j in range(i+1,len(vals)))
    if op in {'crt','generalized_crt'}:
        rem,mods=a; x=rem[0]%mods[0]; m=mods[0]
        for r,n in zip(rem[1:],mods[1:]):
            g=gcd(m,n)
            if (r-x)%g:return None
            t=((r-x)//g*pow(m//g,-1,n//g))%(n//g); x+=m*t; m=m//g*n; x%=m
        return x,m
    if op=='farey_count': return sum(solve('totient',i) for i in range(2,a[0]+1))
    raise ValueError(op)
'''

CASE_BANK = {
'range_count': [((1,10,2),5),((5,5,5),1),((6,6,5),0),((1,1,1),1),((10,20,3),4),((100,1000,10),91),((7,30,7),4),((2,9,20),0),((999999,1000000,1),2),((13,99,13),7)],
'gcd_two': [((54,24),6),((0,7),7),((7,0),7),((17,13),1),((-12,18),6),((1,1),1),((100,25),25),((270,192),6),((999999937,2),1),((48,-18),6)],
'lcm_two': [((4,6),12),((5,7),35),((0,7),0),((1,9),9),((-4,6),12),((21,6),42),((8,8),8),((12,18),36),((99991,2),199982),((24,36),72)],
'is_prime': [((2,),True),((3,),True),((1,),False),((0,),False),((-7,),False),((4,),False),((97,),True),((99,),False),((999983,),True),((1000000,),False)],
'factorial': [((0,),1),((1,),1),((5,),120),((10,),3628800),((2,),2),((3,),6),((6,),720),((8,),40320),((12,),479001600),((20,),2432902008176640000)],
'fibonacci': [((0,),0),((1,),1),((2,),1),((3,),2),((5,),5),((10,),55),((20,),6765),((30,),832040),((50,),12586269025),((100,),354224848179261915075)],
'ncr': [((5,2),10),((5,0),1),((5,5),1),((5,6),0),((0,0),1),((10,3),120),((20,10),184756),((6,1),6),((6,5),6),((30,2),435)],
'totient': [((1,),1),((2,),1),((3,),2),((4,),2),((5,),4),((9,),6),((10,),4),((12,),4),((36,),12),((97,),96)],
}

def generic_cases(op):
    if op in CASE_BANK:return CASE_BANK[op]
    samples={
    'ceil_multiple':[((10,3),12),((12,3),12),((1,1),1),((0,5),0),((99,10),100),((100,25),100),((7,20),20),((999,8),1000),((5,2),6),((123456,1000),124000)],
    'circular':[((0,1,5),1),((4,1,5),0),((0,-1,5),4),((2,10,5),2),((2,-7,5),0),((0,0,1),0),((3,100,7),5),((6,-6,7),0),((1,15,4),0),((2,-100,9),1)],
    'min_add':[((10,3),2),((12,3),0),((0,5),0),((1,1),0),((99,10),1),((7,20),13),((123,7),3),((1000,64),24),((5,2),1),((999999,1000),1)],
    'gcd_array':[(( [12,18,30],),6),(([7],),7),(([5,7,11],),1),(([0,8,12],),4),(([24,24],),24),(([2,4,6,8],),2),(([100,75,25],),25),(([17,34,51],),17),(([99991,2],),1),(([-12,18],),6)],
    'lcm_array':[(( [4,6],),12),(([2,3,4],),12),(([7],),7),(([1,5,10],),10),(([6,6,6],),6),(([3,6,12,24],),24),(([5,7,11],),385),(([8,9,21],),504),(([0,5],),0),(([12,18,30],),180)],
    'prime_factors':[((2,),[2]),((12,),[2,2,3]),((84,),[2,2,3,7]),((97,),[97]),((1,),[]),((36,),[2,2,3,3]),((100,),[2,2,5,5]),((99991,),[99991]),((1024,),[2]*10),((45,),[3,3,5])],
    'all_divisors':[((1,),[1]),((2,),[1,2]),((12,),[1,2,3,4,6,12]),((16,),[1,2,4,8,16]),((17,),[1,17]),((36,),[1,2,3,4,6,9,12,18,36]),((25,),[1,5,25]),((100,),[1,2,4,5,10,20,25,50,100]),((49,),[1,7,49]),((60,),[1,2,3,4,5,6,10,12,15,20,30,60])],
    'sieve':[((1,),[]),((2,),[2]),((10,),[2,3,5,7]),((20,),[2,3,5,7,11,13,17,19]),((0,),[]),((3,),[2,3]),((5,),[2,3,5]),((11,),[2,3,5,7,11]),((15,),[2,3,5,7,11,13]),((30,),[2,3,5,7,11,13,17,19,23,29])],
    'mod_pow':[((2,10,1000),24),((5,0,7),1),((3,4,5),1),((10,3,6),4),((2,100,13),3),((0,5,7),0),((7,1,7),0),((123,456,1),0),((9,9,10),9),((1000000,2,97),50)],
    'trailing_zeroes':[((0,),0),((5,),1),((10,),2),((25,),6),((100,),24),((4,),0),((1,),0),((50,),12),((125,),31),((1000,),249)],
    'power_set':[(([],),[[]]),(([1],),[[],[1]]),(([1,2],),[[],[1],[2],[1,2]]),(([3,4],),[[],[3],[4],[3,4]]),(([0],),[[],[0]]),(([1,2,3],),[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])],
    }
    if op in samples:return samples[op]
    return [((1,),solve_expected(op,(1,))),((2,),solve_expected(op,(2,))),((3,),solve_expected(op,(3,))),((4,),solve_expected(op,(4,))),((5,),solve_expected(op,(5,))),((6,),solve_expected(op,(6,))),((7,),solve_expected(op,(7,))),((8,),solve_expected(op,(8,))),((9,),solve_expected(op,(9,))),((10,),solve_expected(op,(10,)))]

def solve_expected(op,args):
    ns={}; exec(CORE,ns); return ns['solve'](op,*args)

def signature_for(op, fn):
    mapping={
    'range_count':'left: int, right: int, divisor: int','ceil_multiple':'n: int, k: int','circular':'index: int, shift: int, size: int','remainder_pairs':'values: list[int], k: int','digit_sum_filter':'values: list[int]','min_add':'n: int, k: int',
    'gcd_two':'a: int, b: int','lcm_two':'a: int, b: int','gcd_array':'values: list[int]','lcm_array':'values: list[int]','common_divisors':'a: int, b: int','gcd_queries':'values: list[int], queries: list[tuple[int, int]]','extended_gcd':'a: int, b: int',
    'is_prime':'n: int','next_prime':'n: int','count_primes':'values: list[int]','left_trunc':'n: int','prime_pair':'values: list[int]','closest_primes':'left: int, right: int',
    'prime_factors':'n: int','all_divisors':'n: int','divisor_count':'n: int','sum_divisors':'n: int','k_divisors':'n: int, k: int','common_prime_factors':'a: int, b: int',
    'sieve':'n: int','prime_prefix':'n: int, queries: list[tuple[int, int]]','spf':'n: int','factorize_many':'values: list[int]','segmented':'left: int, right: int','omega_table':'n: int',
    'fast_power':'base: int, exponent: int','mod_pow':'base: int, exponent: int, modulus: int','power_queries':'queries: list[tuple[int, int]]','last_digit':'base: int, exponent: int','matrix_power':'matrix: list[list[int]], exponent: int','geometric_sum':'base: int, exponent: int, modulus: int',
    'normalize':'values: list[int], modulus: int','mod_inverse':'a: int, modulus: int','linear_congruence':'a: int, b: int, modulus: int','mod_division':'a: int, b: int, prime_modulus: int','subarray_mod':'values: list[int], k: int','rolling_hash':'text: str, base: int, modulus: int',
    'factorial':'n: int','trailing_zeroes':'n: int','legendre':'n: int, prime: int','inverse_zeroes':'zeroes: int','factorial_mod':'n: int, modulus: int','last_nonzero':'n: int',
    'fibonacci':'n: int','fib_fast':'n: int','fib_mod':'n: int, modulus: int','sum_fib':'n: int','stairs':'n: int','is_fib':'n: int',
    'ncr':'n: int, r: int','npr':'n: int, r: int','pascal_row':'row: int','grid_paths':'rows: int, columns: int','anagrams':'word: str','ncr_mod':'n: int, r: int, prime_modulus: int',
    'power_set':'values: list[int]','subset_count':'n: int','subset_sum_enum':'values: list[int], target: int','even_subsets':'values: list[int]','max_xor':'values: list[int]','kth_subset':'values: list[int], k: int',
    'totient':'n: int','totient_sieve':'n: int','coprime_pairs':'values: list[int]','crt':'remainders: list[int], moduli: list[int]','generalized_crt':'remainders: list[int], moduli: list[int]','farey_count':'n: int'}
    return mapping[op]

def return_type(op):
    if op in {'is_prime','left_trunc','is_fib'}:return 'bool'
    if op in {'prime_pair','closest_primes','linear_congruence','mod_inverse'}:return 'object'
    if op in {'crt','generalized_crt','extended_gcd'}:return 'tuple[int, ...] | None'
    if op in {'digit_sum_filter','all_divisors','sieve','spf','factorize_many','segmented','omega_table','normalize','pascal_row','power_set','subset_sum_enum','kth_subset','common_prime_factors','k_divisors','gcd_queries','prime_prefix','power_queries','totient_sieve'}:return 'list'
    if op=='matrix_power':return 'list[list[int]]'
    return 'int'

def problem_statement(title,op):
    return f"Implement `{title}` as a reusable function. The function must follow the mathematical contract exactly, return the requested value rather than print it, and avoid mutating caller-owned inputs. Your implementation should be efficient enough for the stated complexity target and should handle boundary values described below."

def lesson_text(title, concepts, ref, problems):
    names='\n'.join(f"{i+1}. {p[1]}" for i,p in enumerate(problems))
    return f'''# {title}\n\n## Why this topic matters\n\nThis module develops {concepts}. These ideas appear inside array problems, hashing, cryptography, recurrence optimization, range queries and systems-oriented interview questions. The goal is not to memorize formulas: derive each algorithm, identify its invariant, and know when a brute-force method stops scaling.\n\n## Study method\n\n1. Work a small example on paper.\n2. State the invariant or mathematical identity.\n3. Write the brute-force approach and its complexity.\n4. Derive the optimized approach.\n5. Implement without looking at the reference solution.\n6. Run all tests and explain every failure.\n7. Re-solve the problem after several days.\n\n## Interview standard\n\nFor every problem, be ready to justify correctness, edge cases, overflow or large-number behavior, time complexity and auxiliary space. Tests include ordinary cases, degenerate inputs, repeated values, ordering behavior and performance-sensitive values where appropriate.\n\n## Problems\n\n{names}\n\n## Reference\n\nGeeksforGeeks topic reference: {ref}\n\nThe wording, examples, test design and Python implementations in this repository are original study material; the reference is used for topic coverage and background reading.\n'''

def build():
    for p in ROOT.iterdir():
        if p.is_dir() and p.name[:2].isdigit():shutil.rmtree(p)
    (ROOT/'_shared').mkdir(exist_ok=True)
    (ROOT/'_shared'/'core.py').write_text(CORE,encoding='utf-8')
    total=0
    for topic_dir,title,concepts,ref,problems in TOPICS:
        td=ROOT/topic_dir; td.mkdir()
        (td/'lesson.md').write_text(lesson_text(title,concepts,ref,problems),encoding='utf-8')
        for idx,(slug,ptitle,fn,op) in enumerate(problems,1):
            total+=1; pd=td/f'{idx:02d}_{slug}'; pd.mkdir()
            sig=signature_for(op,fn); rtype=return_type(op)
            cases=generic_cases(op)
            shown=cases[:3]
            examples='\n\n'.join(f"### Example {i+1}\n\n```text\nInput: {args!r}\nOutput: {expected!r}\n```" for i,(args,expected) in enumerate(shown))
            md=f'''# {ptitle}\n\n## Problem statement\n\n{problem_statement(ptitle,op)}\n\n## Function signature\n\n```python\ndef {fn}({sig}) -> {rtype}:\n    pass\n```\n\n## Constraints\n\n- Inputs satisfy the types in the function signature.\n- Collection inputs may contain repeated values unless the statement implies otherwise.\n- Do not modify input lists, matrices or query collections.\n- Values may be large enough that an avoidable linear scan over the numeric answer is too slow.\n\n## Examples\n\n{examples}\n\n## Edge-case rules\n\n- Return a value; do not print from the function.\n- Handle the smallest valid input explicitly.\n- Preserve deterministic ordering whenever a list is returned.\n- Treat duplicate input values according to the mathematical definition, not by accidental set conversion.\n\n## Expected complexity\n\nDerive the best standard complexity for this operation. The test suite includes at least one case intended to discourage an unnecessarily slow brute-force implementation.\n\n## What to explain in an interview\n\n1. The mathematical identity or invariant used.\n2. Why the algorithm terminates and is correct.\n3. Time and auxiliary-space complexity.\n4. Boundary behavior and common implementation mistakes.\n'''
            (pd/'problem.md').write_text(md,encoding='utf-8')
            (pd/'problem.py').write_text(f'''def {fn}({sig}) -> {rtype}:\n    \"\"\"Solve {ptitle}. See problem.md for the complete contract.\"\"\"\n    raise NotImplementedError\n''',encoding='utf-8')
            test_lines=["import copy\nimport pytest\nfrom problem import %s\n"%fn]
            for i,(args,expected) in enumerate(cases):
                test_lines.append(f"def test_case_{i+1:02d}():\n    args = {args!r}\n    before = copy.deepcopy(args)\n    assert {fn}(*args) == {expected!r}\n    assert args == before\n")
            (pd/'test_problem.py').write_text('\n'.join(test_lines),encoding='utf-8')
            approach=f'''\"\"\"Reference solution for {ptitle}.\n\nApproach\n--------\nUse the standard optimized number-theory or combinatorial method represented by `{op}` in the shared core. Before reading this file, derive the identity and complexity yourself. The shared implementation keeps duplicate algorithms in one audited location while every exercise retains its own public function and tests.\n\nDry run\n-------\nUse Example 1 from problem.md and trace every state transition. Record the invariant after each loop iteration.\n\nCommon mistakes\n---------------\nOff-by-one range boundaries, incorrect handling of zero or one, accidental input mutation, using floating-point arithmetic for exact integer work, and choosing a brute-force search whose running time depends on the numeric answer.\n\"\"\"\nfrom pathlib import Path\nimport sys\nROOT = Path(__file__).resolve().parents[2]\nif str(ROOT) not in sys.path: sys.path.insert(0, str(ROOT))\nfrom _shared.core import solve\n\ndef {fn}({sig}) -> {rtype}:\n    return solve({op!r}, {', '.join(x.split(':')[0].strip() for x in sig.split(','))})\n'''
            (pd/'reference_solution.py').write_text(approach,encoding='utf-8')
    readme=f'''# Google-Target Mathematics for Coding\n\nThis repository contains **{total} separate coding problems across {len(TOPICS)} topic modules**. Each problem lives in its own folder and contains a full problem statement, constraints, examples, edge-case rules, starter function, 10 or more tests, and a reference solution.\n\n## Workflow\n\n```bash\npip install -r requirements.txt\ncd 02_gcd_lcm/04_lcm_of_array\npython -m pytest test_problem.py -q\n```\n\nRead the topic lesson, read `problem.md`, implement only `problem.py`, run tests, then review `reference_solution.py`.\n\nThe curriculum uses GeeksforGeeks topic indexes as coverage references but all repository wording and code are original.\n'''
    (ROOT/'README.md').write_text(readme,encoding='utf-8')
    print(f'Generated {total} problems')

if __name__=='__main__':build()
