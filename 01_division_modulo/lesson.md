# Division, Divisibility and Modulo

Integer division answers two different questions: how many complete groups fit, and what remains. For integers `a` and positive `b`, Python guarantees `a = (a // b) * b + (a % b)` and `0 <= a % b < b`. This identity is more useful than memorising `%` as “remainder”, because it explains circular indexing, digit extraction, divisibility, periodic behaviour and interval counting.

A number is divisible by `d` exactly when `n % d == 0`. To count multiples of `d` in `[1, x]`, use `x // d`; therefore the count inside an inclusive interval `[left, right]` is `right // d - (left - 1) // d`. This avoids iterating through the interval. Inclusion–exclusion then lets us count numbers divisible by either of two divisors: count multiples of each and subtract multiples of their LCM, because those were counted twice.

The key interview skill is recognising when a loop over a large numeric range can be replaced by arithmetic. For a range reaching `10^18`, iteration is impossible, while a constant number of divisions is trivial. Be careful with invalid divisors, negative interval endpoints and duplicate divisors. This module restricts the interval to non-negative integers and positive divisors so the mathematical contract is unambiguous.

The consolidated problem asks for counts of numbers divisible by at least one divisor across many queries. A strong solution precomputes nothing proportional to the interval size. It uses GCD to obtain the LCM safely as `(a // gcd(a, b)) * b`, then applies inclusion–exclusion. The expected complexity is `O(q log min(a,b))`, where `q` is the number of queries; auxiliary space is `O(1)` excluding the output.
