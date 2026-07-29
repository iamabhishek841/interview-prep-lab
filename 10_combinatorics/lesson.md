# Permutations, Combinations and nCr

A permutation counts ordered choices; a combination ignores order. The binomial coefficient `C(n,r)` satisfies symmetry `C(n,r)=C(n,n-r)` and Pascal’s identity. Direct factorials are easy but create enormous intermediate values. For exact integer arithmetic, multiply and divide progressively: `result = result*(n-r+i)//i`, after replacing `r` by `min(r,n-r)`.

Many coding problems require `C(n,r) mod p` with prime `p`. When `n < p`, precomputed factorials and inverse factorials allow constant-time queries: `fact[n] * inv_fact[r] * inv_fact[n-r] mod p`. Fermat gives `x^(p-2) mod p` for the inverse. One preprocessing pass serves all queries.

The consolidated problem receives many queries under one prime modulus and a maximum `n` below the modulus. This tests preprocessing, modular inverse and query validation together. Expected time is `O(max_n + log p + q)` and space `O(max_n)`.
