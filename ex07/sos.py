import sys


NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. "
}


def encode_to_morse(text: str) -> str:
    """Encodes a given text string into Morse code.

Parameters
----------
text (str): The text to encode.

Returns
-------
str: The encoded Morse string.
    """

    return ''.join(NESTED_MORSE[c.upper()] for c in text).strip()


def main():
    """Main function that handles the program execution."""

    try:
        assert len(sys.argv) == 2
        assert all(c.upper() in NESTED_MORSE for c in sys.argv[1])

    except AssertionError:
        print("AssertionError: the arguments are bad")
        return

    morse_code = encode_to_morse(sys.argv[1])
    print(morse_code)


if __name__ == "__main__":
    main()
