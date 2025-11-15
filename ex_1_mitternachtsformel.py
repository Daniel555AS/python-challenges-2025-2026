# Write a Python function named mitternachtsformel that takes the three factors 
# of an expression like 'ax^2+bx+c=0' and returns the largest solution, rounded
# to two decimal places.

def mitternachtsformel(a, b, c):
    sqrt_discriminant = (b ** 2 - 4 * a * c) ** 0.5 
    x1 = round((-b + sqrt_discriminant) / (2 * a), 2)
    x2 = round((-b - sqrt_discriminant) / (2 * a), 2)

    return x1 if x1 > x2 else x2


def main() -> None:
    assert mitternachtsformel(2, 8, 2) == -0.27
    assert mitternachtsformel(-7, 7, 3) == 1.32
    print("All tests passed ✓")


if __name__ == '__main__':
    main()
