from __future__ import annotations

from itertools import cycle, islice

import build_course as course


def ten(*cases: tuple) -> list[tuple]:
    """Return exactly ten deterministic, valid argument tuples."""
    return list(islice(cycle(cases), 10))


INPUTS: dict[str, list[tuple]] = {
    "range_count": ten((1, 10, 2), (5, 5, 5), (6, 20, 3), (1, 1, 1), (100, 1000, 10)),
    "ceil_multiple": ten((10, 3), (12, 3), (1, 1), (0, 5), (999, 8)),
    "circular": ten((0, 1, 5), (4, 1, 5), (0, -1, 5), (2, 10, 5), (2, -7, 5)),
    "remainder_pairs": ten(([1, 2, 3, 4], 2), ([5, 5, 5], 3), ([], 7), ([-1, 1, 3], 2), ([10, 20, 30], 10)),
    "digit_sum_filter": ten(([1, 12, 18, 19],), ([10, 11, 21],), ([],), ([100, 111, 128],), ([5, 7, 13],)),
    "min_add": ten((10, 3), (12, 3), (0, 5), (1, 1), (999999, 1000)),
    "gcd_two": ten((54, 24), (0, 7), (17, 13), (-12, 18), (270, 192)),
    "lcm_two": ten((4, 6), (5, 7), (0, 7), (-4, 6), (24, 36)),
    "gcd_array": ten(([12, 18, 30],), ([7],), ([5, 7, 11],), ([0, 8, 12],), ([-12, 18],)),
    "lcm_array": ten(([4, 6],), ([2, 3, 4],), ([7],), ([1, 5, 10],), ([0, 5],)),
    "common_divisors": ten((12, 18), (7, 13), (36, 48), (1, 1), (100, 80)),
    "gcd_queries": ten(([2, 4, 6, 8], [(0, 1), (1, 3)]), ([7], [(0, 0)]), ([12, 18, 30], [(0, 2)])),
    "extended_gcd": ten((30, 20), (17, 13), (0, 5), (-12, 18), (270, 192)),
    "is_prime": ten((2,), (3,), (1,), (97,), (1000000,)),
    "next_prime": ten((1,), (2,), (10,), (97,), (999,)),
    "count_primes": ten(([2, 3, 4, 5],), ([],), ([1, 1, 1],), ([97, 99, 101],), ([-2, 0, 2],)),
    "left_trunc": ten((2,), (23,), (317,), (47,), (103,)),
    "prime_pair": ten(([1, 2, 3],), ([4, 6, 8],), ([10, 3, 8],), ([0, 2],), ([17],)),
    "closest_primes": ten((2, 20), (14, 16), (100, 130), (1, 3), (90, 100)),
    "prime_factors": ten((2,), (12,), (84,), (97,), (1024,)),
    "all_divisors": ten((1,), (2,), (12,), (36,), (100,)),
    "divisor_count": ten((1,), (2,), (12,), (36,), (100,)),
    "sum_divisors": ten((1,), (2,), (12,), (36,), (100,)),
    "k_divisors": ten((10, 2), (20, 4), (1, 1), (30, 3), (50, 6)),
    "common_prime_factors": ten((12, 18), (7, 13), (84, 126), (1, 10), (100, 80)),
    "sieve": ten((0,), (1,), (2,), (10,), (30,)),
    "prime_prefix": ten((20, [(1, 10), (10, 20)]), (2, [(0, 2)]), (100, [(50, 100)])),
    "spf": ten((1,), (2,), (10,), (30,), (100,)),
    "factorize_many": ten(([2, 12, 97],), ([],), ([1, 4, 9],), ([84, 100],), ([1024],)),
    "segmented": ten((1, 10), (14, 30), (100, 130), (2, 2), (90, 100)),
    "omega_table": ten((1,), (2,), (10,), (30,), (100,)),
    "fast_power": ten((2, 10), (5, 0), (-2, 5), (3, 7), (10, 3)),
    "mod_pow": ten((2, 10, 1000), (5, 0, 7), (3, 4, 5), (2, 100, 13), (123, 456, 97)),
    "power_queries": ten(([(2, 3), (3, 2)],), ([],), ([(5, 0)],), ([(-2, 4)],), ([(10, 6)],)),
    "last_digit": ten((2, 10), (5, 0), (9, 9), (10, 100), (123, 456)),
    "matrix_power": ten(([[1, 1], [1, 0]], 0), ([[1, 1], [1, 0]], 1), ([[1, 1], [1, 0]], 5)),
    "geometric_sum": ten((2, 5, 1000), (3, 0, 7), (5, 3, 13), (1, 100, 97), (10, 5, 9)),
    "normalize": ten(([-1, 0, 1], 5), ([10, 20], 7), ([], 3), ([-100], 9), ([5, 6, 7], 5)),
    "mod_inverse": ten((3, 11), (2, 4), (1, 7), (10, 17), (12, 18)),
    "linear_congruence": ten((3, 4, 7), (2, 4, 6), (4, 3, 6), (1, 0, 5), (10, 5, 15)),
    "mod_division": ten((10, 2, 7), (5, 3, 11), (0, 4, 13), (100, 9, 17), (1, 1, 2)),
    "subarray_mod": ten(([4, 5, 0, -2, -3, 1], 5), ([], 3), ([1, 2, 3], 3), ([0, 0], 5), ([-1, 1], 2)),
    "rolling_hash": ten(("abc", 31, 1000000007), ("", 31, 97), ("aaaa", 29, 101), ("Google", 37, 1009), ("123", 53, 997)),
    "factorial": ten((0,), (1,), (5,), (10,), (20,)),
    "trailing_zeroes": ten((0,), (5,), (10,), (25,), (1000,)),
    "legendre": ten((10, 2), (10, 5), (100, 3), (1, 2), (25, 5)),
    "inverse_zeroes": ten((0,), (1,), (6,), (24,), (100,)),
    "factorial_mod": ten((5, 7), (0, 11), (10, 13), (20, 17), (100, 97)),
    "last_nonzero": ten((0,), (1,), (5,), (10,), (25,)),
    "fibonacci": ten((0,), (1,), (2,), (10,), (100,)),
    "fib_fast": ten((0,), (1,), (10,), (100,), (1000,)),
    "fib_mod": ten((10, 7), (0, 5), (1, 2), (100, 13), (1000, 1000000007)),
    "sum_fib": ten((0,), (1,), (5,), (10,), (100,)),
    "stairs": ten((0,), (1,), (2,), (5,), (30,)),
    "is_fib": ten((0,), (1,), (2,), (4,), (144,)),
    "ncr": ten((5, 2), (5, 0), (5, 5), (5, 6), (30, 15)),
    "npr": ten((5, 2), (5, 0), (5, 5), (5, 6), (10, 3)),
    "pascal_row": ten((0,), (1,), (4,), (10,), (20,)),
    "grid_paths": ten((1, 1), (2, 2), (3, 3), (3, 7), (10, 10)),
    "anagrams": ten(("LEVEL",), ("A",), ("AA",), ("ABC",), ("MISSISSIPPI",)),
    "ncr_mod": ten((5, 2, 7), (10, 3, 13), (5, 0, 11), (20, 10, 17), (30, 15, 1000000007)),
    "power_set": ten(([],), ([1],), ([1, 2],), ([1, 2, 3],), ([0, -1],)),
    "subset_count": ten((0,), (1,), (2,), (10,), (20,)),
    "subset_sum_enum": ten(([1, 2, 3], 3), ([], 0), ([0, 0], 0), ([-1, 1], 0), ([2, 4, 6], 5)),
    "even_subsets": ten(([1, 2, 3],), ([],), ([2, 4],), ([1, 3],), ([0, 1],)),
    "max_xor": ten(([1, 2, 3],), ([],), ([8],), ([2, 4, 8],), ([5, 1, 10],)),
    "kth_subset": ten(([1, 2, 3], 0), ([1, 2, 3], 1), ([1, 2, 3], 7), ([], 0), ([5], 1)),
    "totient": ten((1,), (2,), (9,), (36,), (97,)),
    "totient_sieve": ten((1,), (2,), (10,), (30,), (100,)),
    "coprime_pairs": ten(([1, 2, 3],), ([],), ([2, 4, 6],), ([5, 10, 11],), ([7, 13, 21],)),
    "crt": ten(([2, 3], [3, 5]), ([0], [7]), ([1, 2, 3], [2, 3, 5]), ([4, 5], [7, 9]), ([0, 0], [2, 3])),
    "generalized_crt": ten(([2, 6], [4, 8]), ([1, 3], [2, 4]), ([1, 2], [4, 6]), ([0], [5]), ([2, 3], [6, 9])),
    "farey_count": ten((1,), (2,), (5,), (10,), (100,)),
}


STATEMENTS: dict[str, str] = {
    op: (
        "Implement this operation using the function signature below. Return the exact mathematical result, "
        "never print from the function, and do not mutate any caller-owned collection. The examples define "
        "the required input/output contract; your solution must also handle the boundary and performance cases "
        "covered by the tests."
    )
    for op in INPUTS
}

STATEMENTS.update(
    {
        "gcd_two": "Given two integers a and b, return their non-negative greatest common divisor: the largest integer that divides both values exactly. Zero and negative inputs are allowed.",
        "lcm_two": "Given two integers a and b, return their non-negative least common multiple. Return 0 when either input is 0, and avoid overflow-prone multiplication order.",
        "gcd_array": "Given a non-empty list of integers, return the greatest common divisor of every element without changing the list.",
        "lcm_array": "Given a non-empty list of integers, return the least common multiple of all elements. A zero anywhere in the list makes the result zero.",
        "is_prime": "Given an integer n, return True exactly when n is prime. Integers below 2 are not prime; an O(sqrt(n)) test is expected.",
        "prime_factors": "Given a positive integer n, return its prime factors in non-decreasing order, including repeated factors. Return an empty list for n = 1.",
        "sieve": "Given n, return every prime number in the inclusive range [2, n] in ascending order using sieve-style precomputation.",
        "mod_pow": "Return base raised to exponent modulo modulus using binary exponentiation rather than constructing the full power.",
        "trailing_zeroes": "Return the number of trailing decimal zeroes in n! by counting factors of 5; do not calculate n!.",
        "fibonacci": "Return the nth Fibonacci number with F(0)=0 and F(1)=1 using an efficient iterative or logarithmic-time method.",
        "ncr": "Return the exact binomial coefficient n choose r. Return 0 when r is outside [0, n] and exploit symmetry to reduce work.",
        "power_set": "Return all subsets of values in deterministic bitmask order, beginning with the empty subset, without mutating values.",
        "totient": "Return Euler's totient phi(n): the number of integers in [1, n] that are coprime with n.",
        "generalized_crt": "Merge the supplied congruences even when moduli are not pairwise coprime. Return None when they are inconsistent; otherwise return the smallest non-negative solution and combined modulus.",
    }
)


def reliable_cases(op: str):
    args_list = INPUTS[op]
    return [(args, course.solve_expected(op, args)) for args in args_list]


def specific_statement(title: str, op: str) -> str:
    return STATEMENTS[op]


def main() -> None:
    missing = {problem[3] for topic in course.TOPICS for problem in topic[4]} - INPUTS.keys()
    if missing:
        raise RuntimeError(f"Missing test inputs for operations: {sorted(missing)}")

    course.generic_cases = reliable_cases
    course.problem_statement = specific_statement
    course.build()


if __name__ == "__main__":
    main()
