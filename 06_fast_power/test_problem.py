from problem import modular_power_queries as f

def test_basic(): assert f([(2,10,1000)])==[24]
def test_zero_exp(): assert f([(99,0,7)])==[1]
def test_mod_one(): assert f([(2,0,1)])==[0]
def test_negative_base(): assert f([(-2,5,13)])==[7]
def test_exp_one(): assert f([(123,1,50)])==[23]
def test_base_zero(): assert f([(0,5,11)])==[0]
def test_zero_to_zero_contract(): assert f([(0,0,13)])==[1]
def test_many(): assert f([(3,4,5),(10,9,6)])==[1,4]
def test_large_exp(): assert f([(2,10**18,1000000007)])==[719476260]
def test_large_base(): assert f([(10**30+7,12345,97)])==[pow(10**30+7,12345,97)]
def test_input_unchanged():
 x=[(2,10,7)]; y=x.copy(); f(x); assert x==y
