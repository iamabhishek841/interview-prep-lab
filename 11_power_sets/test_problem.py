from problem import target_sum_subsets as f

def test_empty_target(): assert f([],0)==[[]]
def test_empty_miss(): assert f([],1)==[]
def test_basic(): assert f([1,2,3],3)==[[3],[1,2]]
def test_zero_element(): assert f([0,1],0)==[[],[0]]
def test_negatives(): assert f([-3,1,2,4],1)==[[1],[-3,4],[-3,1,2]]
def test_no_solution(): assert f([2,4,8],7)==[]
def test_all_values(): assert f([1,2,4],7)==[[1,2,4]]
def test_negative_target(): assert f([-5,-2,3],-2)==[[-2],[-5,3]]
def test_sorting(): assert f([3,1,2,-1],3)==[[3],[1,2],[3,1,-1]]
def test_input_unchanged():
 x=[1,2,3]; c=x.copy(); f(x,3); assert x==c
def test_twelve_elements():
 vals=list(range(1,13)); out=f(vals,78); assert vals in out
