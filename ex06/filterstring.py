import sys
from ft_filter import ft_filter


def is_num(value: str) -> bool:
    """Check if a parameter is an integer"""

    try:
        int(value)
        return True
    except ValueError:
        return False


def main():
    """Main function to handle input, and filter words by length."""

    try:
        assert len(sys.argv) == 3
        assert is_num(sys.argv[2])

    except AssertionError:
        print("AssertionError: the arguments are bad")
        return

    S = sys.argv[1]
    N = int(sys.argv[2])

    result = ft_filter(lambda word: len(word) > N, S.split())

    print(result)


if __name__ == "__main__":
    main()
