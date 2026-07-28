"""11 — Probability and bit thinking.
Topics: basic probability, expectation, simulation, binary representation, masks, XOR, and subsets.
"""


def probability_of_event(favourable:int,total:int)->float: raise NotImplementedError

def probability_at_least_one_success(p:float,trials:int)->float: raise NotImplementedError

def expected_value(values:list[float],probabilities:list[float])->float: raise NotImplementedError

def count_set_bits(number:int)->int: raise NotImplementedError

def is_power_of_two(number:int)->bool: raise NotImplementedError

def unique_with_xor(values:list[int])->int: raise NotImplementedError

def toggle_bit(number:int,position:int)->int: raise NotImplementedError

def extract_bit(number:int,position:int)->int: raise NotImplementedError

def generate_subsets_with_bits(values:list[int])->list[list[int]]: raise NotImplementedError

def missing_two_numbers(values:list[int],n:int)->tuple[int,int]: raise NotImplementedError

TESTS=[
("probability_of_event",(1,4),0.25),("probability_at_least_one_success",(0.5,2),0.75),
("expected_value",([0,10],[0.7,0.3]),3.0),("count_set_bits",(29,),4),
("is_power_of_two",(64,),True),("unique_with_xor",([4,1,2,1,2],),4),
("toggle_bit",(8,1),10),("extract_bit",(10,3),1),
("generate_subsets_with_bits",([1,2],),[[],[1],[2],[1,2]]),
("missing_two_numbers",([1,2,4,6],6),(3,5))]

def main():
 print("\nSample tests\n"+"-"*50)
 for n,a,e in TESTS[:2]:
  r=globals()[n](*a); assert r==e,f"{n}: expected {e}, got {r}"; print(f"[PASS] {n}")
 print("\nSample tests passed. Running all tests...\n\nFull test suite\n"+"-"*50)
 for n,a,e in TESTS:
  r=globals()[n](*a); assert r==e,f"{n}: expected {e}, got {r}"; print(f"[PASS] {n}")
 print(f"\nOK — {len(TESTS)} questions passed")
if __name__=="__main__": main()
