import sys


def count_characters(text: str) -> None:
    """Counts the number of characters in a text and prints the results.

Prints:
    - The total number of characters
    - The number of upper case letters
    - The number of lower case letters
    - The number of punctuation marks
    - The number of spaces
    - The number of digits

Parameters
----------
text : str
    The text to analyse

Notes
-----
Punctuation marks are defined as any character in the following string:
    !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    """

    string_punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    upper_letters = sum(1 for c in text if c.isupper())
    lower_letters = sum(1 for c in text if c.islower())
    punctuation_marks = sum(1 for c in text if c in string_punctuation)
    spaces = sum(1 for c in text if c.isspace())
    digits = sum(1 for c in text if c.isdigit())
    total_chars = len(text)

    print(f"The text contains {total_chars} characters:")
    print(f"{upper_letters} upper letters")
    print(f"{lower_letters} lower letters")
    print(f"{punctuation_marks} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """Main function

Program handles one string. User input provided if no argument is provided.

Errors
------
AssertionError
    If more than one argument is passed
    """

    args_count = len(sys.argv)

    try:
        assert args_count <= 2, 'more than one argument is provided'

    except AssertionError as error:
        print(f"AssertionError: {error}")

    else:
        if args_count == 2:
            text = sys.argv[1]
        else:
            print('What is the text to count?')
            text = sys.stdin.readline()

        count_characters(text)


if __name__ == "__main__":
    main()