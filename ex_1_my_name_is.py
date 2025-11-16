# Write a Python function named my_name_is that takes a persons name, age and height and 
# returns them in a string like: "My name is name, I am age years old and heightcm tall.".

def my_name_is(name: str, age: int, height: int) -> str:
    return f"My name is {name}, I am {age} years old and {height}cm tall."


def main() -> None:
    assert my_name_is("Bob", 19, 170) == "My name is Bob, I am 19 years old and 170cm tall."
    assert my_name_is("Alice", 18, 165) == "My name is Alice, I am 18 years old and 165cm tall."
    print("All tests passed ✓")


if __name__ == '__main__':
    main()
