"""03 — Sets, mappings, and hashing mathematics.
Topics: uniqueness, membership, frequencies, bijections, grouping, and set algebra.
"""


def unique_count(values: list[int]) -> int: raise NotImplementedError

def common_values(a: list[int], b: list[int]) -> list[int]: raise NotImplementedError

def symmetric_difference(a: list[int], b: list[int]) -> list[int]: raise NotImplementedError

def frequency_map(values: list[str]) -> dict[str,int]: raise NotImplementedError

def first_repeated(values: list[int]) -> int|None: raise NotImplementedError

def are_disjoint(a: list[int], b: list[int]) -> bool: raise NotImplementedError

def is_subset(a: list[int], b: list[int]) -> bool: raise NotImplementedError

def invert_unique_mapping(mapping: dict[str,int]) -> dict[int,str]: raise NotImplementedError

def group_anagrams(words: list[str]) -> list[list[str]]: raise NotImplementedError

def longest_consecutive(values: list[int]) -> int: raise NotImplementedError

TESTS=[
("unique_count",([1,1,2,3],),3),("common_values",([3,1,2],[2,4,3]),[2,3]),
("symmetric_difference",([1,2,3],[3,4]),[1,2,4]),
("frequency_map",(["a","b","a"],),{"a":2,"b":1}),
("first_repeated",([5,2,3,2],),2),("are_disjoint",([1,2],[3,4]),True),
("is_subset",([1,2],[3,2,1]),True),("invert_unique_mapping",({"a":1,"b":2},),{1:"a",2:"b"}),
("group_anagrams",(["eat","tea","bat"],),[["eat","tea"],["bat"]]),
("longest_consecutive",([100,4,200,1,3,2],),4)]

def main():
 print("\nSample tests\n"+"-"*50)
 for n,a,e in TESTS[:2]:
  r=globals()[n](*a); assert r==e,f"{n}{a}: expected {e}, got {r}"; print(f"[PASS] {n}{a}")
 print("\nSample tests passed. Running all tests...\n\nFull test suite\n"+"-"*50)
 for n,a,e in TESTS:
  r=globals()[n](*a); assert r==e,f"{n}{a}: expected {e}, got {r}"; print(f"[PASS] {n}")
 print(f"\nOK — {len(TESTS)} questions passed")
if __name__=="__main__": main()
