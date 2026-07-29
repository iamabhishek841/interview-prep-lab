from problem import synchronisation_plan

def test_pair(): assert synchronisation_plan([4,6])==(12,[3,2])
def test_coprime(): assert synchronisation_plan([5,7])==(35,[7,5])
def test_multiple_values(): assert synchronisation_plan([2,3,4])==(12,[6,4,3])
def test_duplicates(): assert synchronisation_plan([6,6,6])==(6,[1,1,1])
def test_chain(): assert synchronisation_plan([3,6,12,24])==(24,[8,4,2,1])
def test_single(): assert synchronisation_plan([17])==(17,[1])
def test_contains_one(): assert synchronisation_plan([1,5,10])==(10,[10,2,1])
def test_order(): assert synchronisation_plan([15,4,6,10])==(60,[4,15,10,6])
def test_large_shared_factor(): assert synchronisation_plan([999999937,1999999874])==(1999999874,[2,1])
def test_large_coprimes(): assert synchronisation_plan([99991,99989])[0]==9998000099
def test_input_unchanged():
 x=[12,18,30]; y=x.copy(); synchronisation_plan(x); assert x==y
