import sys


def convertToMorse(string) -> str:

    """
        Takes a string and converts it in morse code using a dictionnary
    """
    NESTED_MORSE = {
        # Lettres
        "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
        "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
        "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
        "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
        "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
        "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
        "Y": "-.--",  "Z": "--..",

        # Chiffres
        "0": "-----", "1": ".----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....", "6": "-....", "7": "--...",
        "8": "---..", "9": "----.",

        # Espace
        " ": "/"
    }

    morse = " ".join(NESTED_MORSE[ch] for ch in string.upper())
    return morse


def main():
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        return 1
    try:
        string = str(sys.argv[1])
    except ValueError:
        print("AssertionError: the arguments are bad")
        return 1
    for x in string:
        if not x.isalnum() and not x.isspace():
            print("AssertionError: the arguments are bad")
            return 1
    print(convertToMorse.__doc__)
    convert = convertToMorse(string)
    print(convert)


if __name__ == "__main__":
    main()
