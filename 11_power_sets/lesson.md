# Sets, Subsets and Power Sets

A set of `n` distinct elements has `2^n` subsets because each element independently has two choices: included or excluded. A bit mask from zero through `2^n-1` encodes these choices. Bit `i` indicates whether element `i` is present. This gives a systematic enumeration without recursion.

The full power set is exponentially large, so `O(n*2^n)` time and output space are unavoidable if every subset must be materialised. Interview quality means stating this lower bound instead of claiming an impossible polynomial solution. Nevertheless, many tasks need only subsets satisfying a property; pruning or meet-in-the-middle may then help.

The problem returns all subsets whose sum equals a target, preserving original element order inside each subset and sorting the result first by length and then lexicographically. Input values are distinct but may be negative. This requires correct mask enumeration and deterministic output, while the tests expose assumptions that all values are positive.
