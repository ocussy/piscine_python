import sys


def building(str):
    """
    Count the number of :
    - all characters
    - upper-case characters
    - lower-case characters
    - punctuation characters
    - digits
    - spaces
    """

    upper = 0
    lower = 0
    punc = 0
    digit = 0
    spaces = 0
    for i in str:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isspace():
            spaces += 1
        elif i.isdigit():
            digit += 1
        else:
            punc += 1
    print(f"The text contains {len(str)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punc} punctation marks")
    print(f"{spaces} spaces")
    print(f"{digit} digits")


def main():
    if len(sys.argv) > 2:
        print("Assertion error: more than one argument is provided")
        return 1
    if len(sys.argv) == 1 or not sys.argv[1]:
        print("What is the text to count?")
        str = "Hello World!"
        print(str)
    else:
        str = sys.argv[1]
    print(building.__doc__)
    building(str)


if __name__ == "__main__":
    main()
