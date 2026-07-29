from problem import fibonacci_mod_queries as f

def test_zero(): assert f([(0,10)])==[0]
def test_one(): assert f([(1,10)])==[1]
def test_ten(): assert f([(10,1000)])==[55]
def test_mod_one(): assert f([(100,1)])==[0]
def test_multiple(): assert f([(5,100),(20,1000)])==[5,765]
def test_known_large(): assert f([(100,1000000007)])==[687995182]
def test_huge_index(): assert f([(10**18,1000000007)])==[209783453]
def test_exact_small_mod_large(): assert f([(30,10**18)])==[832040]
def test_recurrence_property():
 vals=f([(1000,99991),(1001,99991),(1002,99991)]); assert vals[2]==(vals[0]+vals[1])%99991
def test_input_unchanged():
 q=[(10,7)]; c=q.copy(); f(q); assert q==c
