import sys


def is_num(n: int) -> bool:
    try:
        int(n)
        return True
    except ValueError:
        return False


if len(sys.argv) != 1:
    arg = sys.argv[1]

    try:
        assert len(sys.argv) == 2, 'more than one argument is provided'
        assert is_num(arg), 'argument is not an integer'

    except AssertionError as error:
        print(f"AssertionError: {error}")

    else:
        if int(arg) % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
