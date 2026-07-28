"""08 — Invariants and correctness.
Topics: conserved quantities, loop invariants, parity arguments, validation, and counterexamples.
"""


def same_parity_sum(values:list[int])->bool: raise NotImplementedError

def permutation_preserves_sum(before:list[int],after:list[int])->bool: raise NotImplementedError

def valid_running_balance(transactions:list[int])->bool: raise NotImplementedError

def find_first_prefix_violation(values:list[int],limit:int)->int|None: raise NotImplementedError

def can_reach_by_plus_two(start:int,target:int)->bool: raise NotImplementedError

def array_rotation_preserves_multiset(a:list[int],b:list[int])->bool: raise NotImplementedError

def verify_sorted_partition(values:list[int],pivot:int)->bool: raise NotImplementedError

def majority_candidate_is_valid(values:list[int],candidate:int)->bool: raise NotImplementedError

def checksum_mod(values:list[int],modulus:int)->int: raise NotImplementedError

def smallest_counterexample_to_claim(claim,limit:int)->int|None: raise NotImplementedError

TESTS=[
("same_parity_sum",([2,4,6],),True),("permutation_preserves_sum",([1,2,3],[3,1,2]),True),
("valid_running_balance",([10,-4,-6],),True),("find_first_prefix_violation",([2,3,8],10),2),
("can_reach_by_plus_two",(3,11),True),("array_rotation_preserves_multiset",([1,2,2],[2,1,2]),True),
("verify_sorted_partition",([1,2,4,7,9],4),True),("majority_candidate_is_valid",([2,2,1,2],2),True),
("checksum_mod",([7,8,9],5),4),("smallest_counterexample_to_claim",(lambda n:n*n>=n,10),None)]

def main():
 print("\nSample tests\n"+"-"*50)
 for n,a,e in TESTS[:2]:
  r=globals()[n](*a); assert r==e,f"{n}: expected {e}, got {r}"; print(f"[PASS] {n}")
 print("\nSample tests passed. Running all tests...\n\nFull test suite\n"+"-"*50)
 for n,a,e in TESTS:
  r=globals()[n](*a); assert r==e,f"{n}: expected {e}, got {r}"; print(f"[PASS] {n}")
 print(f"\nOK — {len(TESTS)} questions passed")
if __name__=="__main__": main()
