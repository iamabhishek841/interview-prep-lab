from problem import is_two_sided_truncatable_prime as f

def test_two(): assert f(2)
def test_single_digit_prime(): assert f(7)
def test_one(): assert not f(1)
def test_zero(): assert not f(0)
def test_negative(): assert not f(-37)
def test_composite(): assert not f(49)
def test_contains_zero(): assert not f(103)
def test_left_only_not_enough(): assert not f(317)
def test_right_only_not_enough(): assert not f(3797)
def test_two_sided_23(): assert f(23)
def test_two_sided_37(): assert f(37)
def test_known_large(): assert f(3137)
