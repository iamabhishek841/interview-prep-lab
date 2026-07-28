"""04 — Functions and relations.
Topics: composition, inverse mappings, monotonicity, injectivity, periodicity, and closures.
"""


def compose(f, g, value): raise NotImplementedError

def apply_repeatedly(function, value, times: int): raise NotImplementedError

def is_injective(mapping: dict) -> bool: raise NotImplementedError

def is_surjective(mapping: dict, codomain: set) -> bool: raise NotImplementedError

def inverse_mapping(mapping: dict) -> dict: raise NotImplementedError

def is_non_decreasing(values: list[int]) -> bool: raise NotImplementedError

def fixed_points(function, values: list[int]) -> list[int]: raise NotImplementedError

def relation_is_reflexive(pairs: set[tuple], elements: set) -> bool: raise NotImplementedError

def relation_is_symmetric(pairs: set[tuple]) -> bool: raise NotImplementedError

def transitive_closure(edges: list[tuple[str,str]]) -> set[tuple[str,str]]: raise NotImplementedError

TESTS=[
("compose",(lambda x:x+1,lambda x:x*2,3),7),
("apply_repeatedly",(lambda x:x+2,1,3),7),
("is_injective",({"a":1,"b":2},),True),
("is_surjective",({"a":1,"b":2},{1,2}),True),
("inverse_mapping",({"a":1,"b":2},),{1:"a",2:"b"}),
("is_non_decreasing",([1,1,3,7],),True),
("fixed_points",(lambda x:x*x,[0,1,2]),[0,1]),
("relation_is_reflexive",({(1,1),(2,2)},{1,2}),True),
("relation_is_symmetric",({(1,2),(2,1)},),True),
("transitive_closure",([("a","b"),("b","c")],),{("a","b"),("b","c"),("a","c")})]

def main():
 print("\nSample tests\n"+"-"*50)
 for n,a,e in TESTS[:2]:
  r=globals()[n](*a); assert r==e,f"{n}: expected {e}, got {r}"; print(f"[PASS] {n}")
 print("\nSample tests passed. Running all tests...\n\nFull test suite\n"+"-"*50)
 for n,a,e in TESTS:
  r=globals()[n](*a); assert r==e,f"{n}: expected {e}, got {r}"; print(f"[PASS] {n}")
 print(f"\nOK — {len(TESTS)} questions passed")
if __name__=="__main__": main()
