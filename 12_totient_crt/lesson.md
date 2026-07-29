# Euler Totient, Modular Inverse and Chinese Remainder Theorem

Euler’s totient `phi(n)` counts integers in `[1,n]` coprime to `n`. From prime factorisation, `phi(n)=n * product(1-1/p)` over distinct prime factors. Compute it with integer updates `result -= result//p` while factoring.

The Chinese Remainder Theorem combines congruences. For pairwise-coprime moduli, a unique solution exists modulo their product. More generally, two congruences `x≡a1 mod m1` and `x≡a2 mod m2` are compatible exactly when `a2-a1` is divisible by `gcd(m1,m2)`. Divide by the gcd, solve a modular linear equation using an inverse, and normalise the smallest non-negative result. The combined modulus is the LCM, not always the product.

The final problem merges a list of congruences one by one and also returns the totient of the combined modulus. Returning `None` for an inconsistent system is essential. This is advanced material: derive the pair-combination equation on paper before coding. Complexity is logarithmic per merge, plus factorisation of the final modulus for the totient.
