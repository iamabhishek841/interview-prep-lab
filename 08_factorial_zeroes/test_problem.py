from problem import minimum_factorials_for_zeroes as f

def test_zero(): assert f([0])==[0]
def test_one(): assert f([1])==[5]
def test_four(): assert f([4])==[20]
def test_five(): assert f([5])==[25]
def test_six(): assert f([6])==[25]
def test_twenty_four(): assert f([24])==[100]
def test_twenty_five(): assert f([25])==[105]
def test_many(): assert f([0,1,2,3])==[0,5,10,15]
def test_large(): assert f([1000000000])==[4000000015]
def test_minimality():
 for k,n in zip(range(1,200),f(list(range(1,200)))):
  def z(x):
   s=0
   while x:x//=5;s+=x
   return s
  assert z(n)>=k and z(n-1)<k
