# Write a Python function named insert_string that takes as arguments
# a original string, a index in that string and a new string. It should 
#return the original string with the new string inserted at the given index.

def insert_string(original_string: str, loc: int, to_insert: str) -> str:
    return original_string[0: loc] + to_insert + original_string[loc:] 


def main() -> None:
    assert insert_string("Hello rld!", 6, "Wo") == "Hello World!"
    assert insert_string("", 0, "Test") == "Test"
    assert insert_string("Cy", 2, "Sec") == "CySec"
    print("All tests passed ✓")


if __name__ == '__main__':
    main()
