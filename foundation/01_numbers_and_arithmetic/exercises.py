"""01 — Numbers and arithmetic

Concepts: divisibility, integer division, modulo, digit maths, GCD/LCM,
fast powers, circular arithmetic, and interval counting.
Solve top to bottom, then press Run in VS Code.
"""


def is_divisible(number: int, divisor: int) -> bool:
    raise NotImplementedError


def digit_sum(number: int) -> int:
    raise NotImplementedError


def reverse_integer(number: int) -> int:
    raise NotImplementedError


def gcd(a: int, b: int) -> int:
    raise NotImplementedError


def lcm(a: int, b: int) -> int:
    raise NotImplementedError


def count_multiples(left: int, right: int, divisor: int) -> int:
    raise NotImplementedError


def fast_power(base: int, exponent: int) -> int:
    raise NotImplementedError


def modular_power(base: int, exponent: int, modulus: int) -> int:
    raise NotImplementedError


def rotate_index(index: int, shift: int, size: int) -> int:
    raise NotImplementedError


def missing_number(values: list[int], n: int) -> int:
    """Values contain distinct numbers from 0..n with one missing."""
    raise NotImplementedError


TESTS = [
    ("is_divisible", (18, 3), True),
    ("digit_sum", (-507,), 12),
    ("reverse_integer", (-120,), -21),
    ("gcd", (54, 24), 6),
    ("lcm", (12, 18), 36),
    ("count_multiples", (5, 20, 4), 4),
    ("fast_power", (3, 5), 243),
    ("modular_power", (2, 10, 1000), 24),
    ("rotate_index", (1, -3, 5), 3),
    ("missing_number", ([3, 0, 1], 3), 2),
]


def main() -> None:
    print("\nSample tests\n" + "-" * 50)
    for name, args, expected in TESTS[:2]:
        actual = globals()[name](*args)
        assert actual == expected, f"{name}{args}: expected {expected}, got {actual}"
        print(f"[PASS] {name}{args}")
    print("\nSample tests passed. Running all tests...\n\nFull test suite\n" + "-" * 50)
    for name, args, expected in TESTS:
        actual = globals()[name](*args)
        assert actual == expected, f"{name}{args}: expected {expected}, got {actual}"
        print(f"[PASS] {name}")
    print(f"\nOK — {len(TESTS)} questions passed")


if __name__ == "__main__":
    main()
