# Write a Python function named square_root that takes a 
# number n and returns the square root of n, rounded to two 
# decimal places. You can expect the input to always be positive.

def square_root(n: int) -> float:
    return round(n ** 0.5, 2)


def main() -> None:
    assert square_root(3) == 1.73
    assert square_root(16) == 4.0
    assert square_root(1337) == 36.57
    print("All tests passed ✓")


if __name__ == '__main__':
    main()
