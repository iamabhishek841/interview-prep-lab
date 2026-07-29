# Factorials and Trailing Zeroes

A trailing decimal zero is created by a factor ten, and `10 = 2*5`. In `n!`, factors of two are much more abundant than factors of five, so the number of trailing zeroes equals the exponent of five in the prime factorisation of `n!`. Count multiples of five, then multiples of twenty-five contribute an additional five, multiples of one hundred twenty-five another, and so on: `floor(n/5)+floor(n/25)+...`.

The inverse problem is more interesting: find the smallest `n` whose factorial has at least `k` trailing zeroes. The zero-count function is monotonic, enabling binary search. A safe upper bound is `5*k` for positive `k`; zero itself handles `k=0`. At each midpoint, discard the half that cannot contain the first valid answer.

This combines number theory and search-on-answer, a recurring interview pattern. Computing factorial is unnecessary and catastrophic for large inputs. Expected complexity is `O(log k * log_5 k)` time and constant space.
