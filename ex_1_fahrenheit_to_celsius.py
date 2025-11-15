# Write a Python function named fahrenheit_to_celsius that converts 
# a given Fahrenheit temperature to Celsius, rounded to two decimal 
# places and returns it.

def fahrenheit_to_celsius(f: int) -> float:
    return round((f - 32) * (5 / 9), 2)


def main() -> None:
    assert fahrenheit_to_celsius(98) == 36.67
    assert fahrenheit_to_celsius(-35) == -37.22
    assert fahrenheit_to_celsius(1337) == 725.0
    print("All tests passed ✓")


if __name__ == '__main__':
    main()
