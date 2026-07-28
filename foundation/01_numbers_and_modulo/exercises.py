from pathlib import Path
import unittest


def is_even(number: int) -> bool:
    """Return True when number is even."""
    return number % 2 == 0


def circular_index(index: int, size: int) -> int:
    """Return the valid circular index for a collection of the given size."""
    return index % size


def count_complete_groups(total: int, group_size: int) -> int:
    """Return how many complete groups can be formed."""
    return total // group_size


def remaining_items(total: int, group_size: int) -> int:
    """Return how many items remain after forming complete groups."""
    return total % group_size


def run_sample_tests() -> bool:
    """Run two visible checks before the complete local test suite."""
    samples = [
        ("is_even(8)", lambda: is_even(8), True),
        ("remaining_items(17, 5)", lambda: remaining_items(17, 5), 2),
    ]

    print("\nSample tests")
    print("-" * 50)

    all_passed = True
    for name, operation, expected in samples:
        try:
            actual = operation()
            passed = actual == expected
        except Exception as error:  # Show learner-friendly output.
            actual = f"{type(error).__name__}: {error}"
            passed = False

        status = "PASS" if passed else "FAIL"
        print(f"[{status}] {name}")
        if not passed:
            print(f"       expected: {expected!r}")
            print(f"       received: {actual!r}")
            all_passed = False

    return all_passed


def run_full_test_suite() -> bool:
    """Run every test from this lesson without changing folders."""
    lesson_directory = Path(__file__).resolve().parent
    suite = unittest.defaultTestLoader.discover(
        start_dir=str(lesson_directory),
        pattern="test_exercises.py",
    )

    print("\nFull test suite")
    print("-" * 50)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return result.wasSuccessful()


def main() -> None:
    """Provide a one-click, LeetCode-style local test experience."""
    if not run_sample_tests():
        print("\nFix the sample tests first. Full tests were not run.")
        raise SystemExit(1)

    print("\nSample tests passed. Running all tests...")
    if not run_full_test_suite():
        raise SystemExit(1)

    print("\nAll tests passed. Lesson complete!")


if __name__ == "__main__":
    main()


