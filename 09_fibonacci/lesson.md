# Fibonacci Numbers and Recurrences

The Fibonacci recurrence `F(n)=F(n-1)+F(n-2)` describes overlapping subproblems. Naive recursion recomputes the same values exponentially. Iteration reduces this to linear time and constant space. For very large `n`, matrix exponentiation or fast doubling reaches logarithmic time.

Fast doubling derives both `F(2k)` and `F(2k+1)` from `F(k)` and `F(k+1)`: `F(2k)=F(k)*(2*F(k+1)-F(k))` and `F(2k+1)=F(k)^2+F(k+1)^2`. Recursing on `n//2` therefore halves the index each step. Modulo can be applied throughout.

The problem asks for Fibonacci values modulo `m` for indexes as large as `10^18`. A linear loop is intentionally too slow. A recursive helper returning the pair `(F(n),F(n+1))` is concise and avoids matrix boilerplate. Expected complexity is `O(log n)` time and `O(log n)` recursion depth.
