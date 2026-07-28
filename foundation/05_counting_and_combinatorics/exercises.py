"""05 — Counting and combinatorics.
Topics: factorials, permutations, combinations, Pascal rows, subsets, and counting paths.
"""


def factorial(n:int)->int: raise NotImplementedError

def permutations(n:int,r:int)->int: raise NotImplementedError

def combinations(n:int,r:int)->int: raise NotImplementedError

def pascal_row(n:int)->list[int]: raise NotImplementedError

def subset_count(n:int)->int: raise NotImplementedError

def non_empty_subset_count(n:int)->int: raise NotImplementedError

def grid_paths(rows:int,cols:int)->int: raise NotImplementedError

def count_binary_strings_without_consecutive_ones(n:int)->int: raise NotImplementedError

def count_anagram_arrangements(word:str)->int: raise NotImplementedError

def kth_permutation(items:list[int],k:int)->list[int]: raise NotImplementedError

TESTS=[
("factorial",(5,),120),("permutations",(5,2),20),("combinations",(5,2),10),
("pascal_row",(4,),[1,4,6,4,1]),("subset_count",(5,),32),
("non_empty_subset_count",(3,),7),("grid_paths",(3,3),6),
("count_binary_strings_without_consecutive_ones",(4,),8),
("count_anagram_arrangements",("LEVEL",),30),("kth_permutation",([1,2,3],4),[2,3,1])]

def main():
 print("\nSample tests\n"+"-"*50)
 for n,a,e in TESTS[:2]:
  r=globals()[n](*a); assert r==e,f"{n}: expected {e}, got {r}"; print(f"[PASS] {n}")
 print("\nSample tests passed. Running all tests...\n\nFull test suite\n"+"-"*50)
 for n,a,e in TESTS:
  r=globals()[n](*a); assert r==e,f"{n}: expected {e}, got {r}"; print(f"[PASS] {n}")
 print(f"\nOK — {len(TESTS)} questions passed")
if __name__=="__main__": main()
