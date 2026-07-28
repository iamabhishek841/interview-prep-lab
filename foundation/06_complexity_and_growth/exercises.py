"""06 — Complexity and growth.
Topics: operation counting, logarithms, dominant terms, loop growth, and asymptotic comparison.
"""


def linear_operations(n:int)->int: raise NotImplementedError

def triangular_operations(n:int)->int: raise NotImplementedError

def binary_halving_steps(n:int)->int: raise NotImplementedError

def powers_until_limit(base:int,limit:int)->int: raise NotImplementedError

def nested_rectangular_operations(n:int,m:int)->int: raise NotImplementedError

def dominant_complexity(terms:list[tuple[int,int]])->int: raise NotImplementedError

def compare_growth(n:int)->str: raise NotImplementedError

def recursion_tree_nodes(branches:int,depth:int)->int: raise NotImplementedError

def amortized_resize_cost(appends:int)->int: raise NotImplementedError

def smallest_n_where_nlogn_beats_square(start:int)->int: raise NotImplementedError

TESTS=[
("linear_operations",(8,),8),("triangular_operations",(4,),10),
("binary_halving_steps",(16,),4),("powers_until_limit",(2,20),5),
("nested_rectangular_operations",(3,5),15),("dominant_complexity",([(4,1),(2,3),(7,2)],),3),
("compare_growth",(16,),"nlogn"),("recursion_tree_nodes",(2,3),15),
("amortized_resize_cost",(8,),15),("smallest_n_where_nlogn_beats_square",(2,),2)]

def main():
 print("\nSample tests\n"+"-"*50)
 for n,a,e in TESTS[:2]:
  r=globals()[n](*a); assert r==e,f"{n}: expected {e}, got {r}"; print(f"[PASS] {n}")
 print("\nSample tests passed. Running all tests...\n\nFull test suite\n"+"-"*50)
 for n,a,e in TESTS:
  r=globals()[n](*a); assert r==e,f"{n}: expected {e}, got {r}"; print(f"[PASS] {n}")
 print(f"\nOK — {len(TESTS)} questions passed")
if __name__=="__main__": main()
