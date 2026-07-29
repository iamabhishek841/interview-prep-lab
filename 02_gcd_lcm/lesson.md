# GCD, LCM and the Euclidean Algorithm

The greatest common divisor of two integers is the largest positive integer dividing both. Euclid’s algorithm rests on the invariant `gcd(a,b) = gcd(b, a % b)`. Replacing the larger pair with a smaller pair preserves the set of common divisors, and the second component strictly decreases until it becomes zero. The remaining non-zero value is the GCD. This gives logarithmic time rather than scanning every possible divisor.

The least common multiple is connected by `gcd(a,b) * lcm(a,b) = |a*b|` for non-zero integers. In fixed-width languages, calculate `(a // gcd(a,b)) * b` to reduce overflow risk. Python integers do not overflow, but using the safer form demonstrates sound algorithmic habits.

For an array, fold the pairwise operation: `gcd(gcd(a,b),c)` and `lcm(lcm(a,b),c)`. GCD is associative and commutative, so input order does not matter. For LCM, the presence of `1` changes nothing, duplicates change nothing, and if one value divides the current LCM then the result remains unchanged.

The problem combines both operations: determine the smallest positive synchronisation time shared by all periods, then report how many cycles each process completes by that time. This forces you to compute an array LCM without brute-force searching through timestamps. Large coprime values make repeated-increment approaches time out. Expected complexity is `O(n log M)` and `O(n)` output space.
