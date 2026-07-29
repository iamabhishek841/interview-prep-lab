# Prime Numbers and Primality Testing

A prime is an integer greater than one with exactly two positive divisors. The central optimisation is the square-root boundary. If `n = a*b` is composite and both factors were greater than `sqrt(n)`, their product would exceed `n`; therefore at least one factor is at most `sqrt(n)`. A deterministic trial-division test only needs to inspect candidates up to `isqrt(n)`.

Handle `n < 2`, then remove even numbers immediately. Checking only odd divisors halves the work. For many repeated queries within a bounded range, a sieve is superior; for a small number of arbitrary values, direct testing avoids allocating an array up to the maximum value. Choosing between these strategies is part of the interview, not an implementation detail.

Digit-truncation problems add a representation decision. String slicing is readable and normally acceptable; arithmetic truncation avoids conversion but is easier to get wrong. The course problem asks for a two-sided truncatable prime: the original number and every number created by repeatedly removing one digit from the left must be prime, and the same must hold when removing from the right. Zero is rejected because truncation would create leading-zero ambiguity.

A correct solution performs only a logarithmic number of primality checks because an integer has `O(log n)` digits. Each direct check costs `O(sqrt n)` in the worst case. It must short-circuit immediately when any truncation is composite. The tests include single-digit primes, composites, zeros inside the number and a known multi-digit valid chain.
