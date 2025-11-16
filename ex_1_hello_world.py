# Write a Python function named hello_world that simply returns the string "Hello World!".

def hello_world():
    hello_world = [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 33]

    return "".join(chr(value) for value in hello_world)


def main():
    assert hello_world() == 'Hello World!'
    print("All tests passed ✓")


if __name__ == '__main__':
    main()
