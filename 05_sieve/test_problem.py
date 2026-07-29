from problem import prime_count_queries as f

def test_empty(): assert f([])==[]
def test_basic(): assert f([(1,10)])==[4]
def test_zero_one(): assert f([(0,1)])==[0]
def test_two(): assert f([(2,2)])==[1]
def test_composite_single(): assert f([(9,9)])==[0]
def test_multiple(): assert f([(1,10),(10,20)])==[4,4]
def test_no_primes(): assert f([(14,16)])==[0]
def test_full_small(): assert f([(0,30)])==[10]
def test_boundary_prime(): assert f([(29,29)])==[1]
def test_large(): assert f([(1,1000000)])==[78498]
def test_input_unchanged():
 x=[(1,10),(2,3)]; y=x.copy(); f(x); assert x==y
