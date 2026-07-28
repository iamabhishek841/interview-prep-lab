"""02 — Logic and Boolean reasoning.
Topics: truth conditions, XOR, implication, validation, interval overlap, and state rules.
"""


def exactly_one(a: bool, b: bool) -> bool: raise NotImplementedError

def at_least_two(a: bool, b: bool, c: bool) -> bool: raise NotImplementedError

def implies(a: bool, b: bool) -> bool: raise NotImplementedError

def all_equal(values: list[object]) -> bool: raise NotImplementedError

def valid_triangle(a: int, b: int, c: int) -> bool: raise NotImplementedError

def intervals_overlap(a1: int, a2: int, b1: int, b2: int) -> bool: raise NotImplementedError

def can_access(is_admin: bool, is_owner: bool, is_blocked: bool) -> bool: raise NotImplementedError

def is_leap_year(year: int) -> bool: raise NotImplementedError

def balanced_parentheses(text: str) -> bool: raise NotImplementedError

def evaluate_postfix_boolean(tokens: list[str]) -> bool: raise NotImplementedError

TESTS=[
("exactly_one",(True,False),True),("at_least_two",(True,False,True),True),
("implies",(True,False),False),("all_equal",([4,4,4],),True),
("valid_triangle",(3,4,5),True),("intervals_overlap",(1,5,5,8),True),
("can_access",(False,True,False),True),("is_leap_year",(2000,),True),
("balanced_parentheses",("(()())",),True),
("evaluate_postfix_boolean",(["T","F","OR","T","AND"],),True)]

def main():
 print("\nSample tests\n"+"-"*50)
 for n,a,e in TESTS[:2]:
  r=globals()[n](*a); assert r==e,f"{n}{a}: expected {e}, got {r}"; print(f"[PASS] {n}{a}")
 print("\nSample tests passed. Running all tests...\n\nFull test suite\n"+"-"*50)
 for n,a,e in TESTS:
  r=globals()[n](*a); assert r==e,f"{n}{a}: expected {e}, got {r}"; print(f"[PASS] {n}")
 print(f"\nOK — {len(TESTS)} questions passed")
if __name__=="__main__": main()
