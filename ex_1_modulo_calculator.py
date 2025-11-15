# Write a Python function named modulo_calculator that two numbers 
# a and n and returns the string: "a modulo n is result".
# You don't need to worry about illegal inputs (like n=0).

def calculate_modulo(a: int, n: int) -> str:
    return f"{a} modulo {n} is {a % n}"


def main() -> None:
    assert calculate_modulo(6, 2) == "6 modulo 2 is 0"
    assert calculate_modulo(1337, 42) == "1337 modulo 42 is 35"
    assert calculate_modulo(-25, 4) == "-25 modulo 4 is 3"
    print("All tests passed ✓")

if __name__ == "__main__":
    main()
