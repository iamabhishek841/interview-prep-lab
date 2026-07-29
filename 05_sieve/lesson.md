# Sieve of Eratosthenes

A primality test answers one number; a sieve preprocesses an entire bounded domain. Begin by assuming every integer from two through `limit` is prime. When a prime `p` is found, mark its multiples composite. Marking can start at `p*p`, because smaller multiples such as `2p` and `3p` were already handled by smaller prime factors. Processing only while `p*p <= limit` is sufficient.

The classic sieve costs `O(n log log n)` time and `O(n)` memory. It is ideal when many later queries ask about primes below a fixed maximum. A prefix-count array transforms each range query into constant time: `count[right] - count[left-1]`. This pattern—preprocessing plus cheap queries—is common in Google interviews.

The consolidated problem takes many inclusive ranges and returns the number of primes in each. The maximum endpoint may be one million and the number of queries may be large, so calling trial division for every integer in every query wastes repeated work. Build one sieve up to the global maximum, then one prefix array.

Correct boundary handling matters: zero and one are not prime, a range may contain no primes, and `[2,2]` contains exactly one. Input must not be modified. Expected complexity is `O(M log log M + q)` time and `O(M)` space, where `M` is the largest right endpoint.
