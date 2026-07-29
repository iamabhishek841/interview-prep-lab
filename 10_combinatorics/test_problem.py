from problem import combination_queries as f
P=1000000007

def test_empty(): assert f([],P)==[]
def test_zero_zero(): assert f([(0,0)],P)==[1]
def test_basic(): assert f([(5,2)],P)==[10]
def test_edges(): assert f([(7,0),(7,7)],P)==[1,1]
def test_invalid_high(): assert f([(5,6)],P)==[0]
def test_invalid_negative(): assert f([(5,-1)],P)==[0]
def test_symmetry(): assert f([(100,3),(100,97)],P)==[161700,161700]
def test_many(): assert f([(5,2),(6,3),(10,5)],P)==[10,20,252]
def test_large_n(): assert f([(100000,50000)],P)==[149033233]
def test_small_prime(): assert f([(6,2),(6,4)],7)==[1,1]
def test_input_unchanged():
 q=[(5,2)]; c=q.copy(); f(q,P); assert q==c
