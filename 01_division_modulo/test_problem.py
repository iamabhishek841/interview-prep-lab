from problem import count_divisible_queries

def test_basic(): assert count_divisible_queries([(1,10,2,3)])==[7]
def test_single_point_hit(): assert count_divisible_queries([(6,6,2,3)])==[1]
def test_single_point_miss(): assert count_divisible_queries([(5,5,2,3)])==[0]
def test_zero_included(): assert count_divisible_queries([(0,0,7,11)])==[1]
def test_equal_divisors(): assert count_divisible_queries([(1,20,4,4)])==[5]
def test_one_divisor_is_one(): assert count_divisible_queries([(0,99,1,17)])==[100]
def test_nested_divisors(): assert count_divisible_queries([(1,30,3,6)])==[10]
def test_non_coprime(): assert count_divisible_queries([(1,100,6,8)])==[25]
def test_many_queries(): assert count_divisible_queries([(1,10,2,5),(10,20,4,6)])==[6,4]
def test_large_range(): assert count_divisible_queries([(1,10**18,2,5)])==[600000000000000000]
def test_input_unchanged():
 q=[(1,10,2,3)]; copy=q.copy(); count_divisible_queries(q); assert q==copy
