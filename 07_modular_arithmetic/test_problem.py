from problem import modular_division_queries as f

def test_basic(): assert f([(10,3,7)])==[1]
def test_inverse_one(): assert f([(8,1,5)])==[3]
def test_no_inverse(): assert f([(10,4,6)])==[None]
def test_zero_numerator(): assert f([(0,3,11)])==[0]
def test_negative_numerator(): assert f([(-5,3,7)])==[3]
def test_negative_denominator(): assert f([(5,-3,7)])==[3]
def test_denominator_multiple_mod(): assert f([(5,14,7)])==[None]
def test_nonprime_modulus_valid(): assert f([(7,5,12)])==[11]
def test_many(): assert f([(4,2,7),(6,3,9)])==[2,None]
def test_large_modulus(): assert f([(123456789,987654321,1000000007)])==[203935601]
def test_identity_check():
 n,d,m=98765,4321,99991; r=f([(n,d,m)])[0]; assert r is not None and r*d%m==n%m
