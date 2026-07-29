# Google-Target Mathematics for Coding

This repository is being rebuilt as a complete mathematics-for-coding interview course with 72 separate problems across 12 topic modules.

Each exercise has its own folder containing:

- `problem.md` with a full statement, function signature, constraints, examples, edge-case rules and interview discussion points;
- `problem.py` with the starter function;
- `test_problem.py` with 10 or more correctness, edge-case, immutability and performance-sensitive tests;
- `reference_solution.py` for review after a genuine attempt.

## Workflow

```bash
pip install -r requirements.txt
cd 02_gcd_lcm/04_lcm_of_array
python -m pytest test_problem.py -q
```

Read the topic lesson first, implement only `problem.py`, run the tests, and inspect the reference solution only after solving or completing a serious timed attempt.

The topic coverage uses GeeksforGeeks mathematical-algorithm indexes as references. The repository's wording, test design and Python implementations are original study material.
