from problem import solve_congruence_system as f

def test_empty(): assert f([])==(0,1,1)
def test_single(): assert f([(2,5)])==(2,5,4)
def test_coprime_pair(): assert f([(2,3),(3,5)])==(8,15,8)
def test_three(): assert f([(2,3),(3,5),(2,7)])==(23,105,48)
def test_non_coprime_consistent(): assert f([(2,4),(6,8)])==(6,8,4)
def test_non_coprime_inconsistent(): assert f([(1,2),(0,4)]) is None
def test_negative_remainder(): assert f([(-1,5),(1,2)])==(9,10,4)
def test_redundant(): assert f([(3,7),(3,7)])==(3,7,6)
def test_nested_moduli(): assert f([(5,6),(17,24)])==(17,24,8)
def test_large():
 r=f([(12345,99991),(54321,99989)]); assert r is not None and r[0]%99991==12345 and r[0]%99989==54321
def test_phi_prime_product(): assert f([(0,11),(0,13)])==(0,143,120)
