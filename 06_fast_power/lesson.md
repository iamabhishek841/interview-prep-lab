# Fast Exponentiation

Naive exponentiation multiplies the base `exponent` times. Binary exponentiation uses the exponent’s binary representation. If the exponent is even, `a^n = (a^(n/2))^2`; if odd, remove one factor of `a` and continue. Iteratively, maintain an invariant: `result * base^exponent` always equals the original target. When the current low bit is one, multiply it into the result; square the base and halve the exponent.

This reduces multiplication count from `O(n)` to `O(log n)`. With a modulus, reduce after every multiplication to prevent enormous intermediate values. Python’s built-in `pow(base, exp, mod)` is highly optimised, but interviews often require implementing the method to demonstrate the reasoning.

The problem evaluates many power towers of the form `base^exponent mod modulus`, including huge exponents. It explicitly forbids constructing the full power first. Edge cases include exponent zero, modulus one, negative bases and large values. Python modulo normalises negative bases into the required residue class.

Expected complexity is `O(q log exponent)` time and constant auxiliary space. The tests include an exponent around `10^18`, which makes linear multiplication infeasible.
