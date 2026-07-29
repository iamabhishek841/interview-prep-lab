# Modular Arithmetic and Inverses

Congruence `a ≡ b (mod m)` means `m` divides `a-b`. Addition and multiplication can be reduced at every step without changing the final residue. Division is different: dividing by `b` modulo `m` means multiplying by a modular inverse `b^-1`, which exists exactly when `gcd(b,m)=1`.

The extended Euclidean algorithm finds integers `x,y` satisfying `ax+my=gcd(a,m)`. When the gcd is one, `ax ≡ 1 (mod m)`, so `x mod m` is the inverse. This works for non-prime moduli, unlike Fermat’s little theorem, which requires a prime modulus and a non-multiple of it.

The problem evaluates modular fractions `(numerator / denominator) mod modulus` for many triples. It must return `None` when division is impossible. This tests the distinction between ordinary integer division and modular division, and it forces careful normalisation of negative coefficients.

Expected time is logarithmic in the modulus per query and constant auxiliary space. Do not brute-force candidate inverses from one upward; a modulus near one billion would expose that immediately.
