from ft_filter import ft_filter
import sys


def isBigger(word, num):
    """
        isBigger(word, num)
        Search if the word given has a len bigger than the num
    """
    if len(word) > num:
        return True
    return False


def main():
    if len(sys.argv) != 3:
        print("AssertionError : the arguments are bad")
        return 1
    try:
        string = str(sys.argv[1])
        num = int(sys.argv[2])
    except ValueError:
        print("AssertionError : the arguments are bad")
        return 1
    array = string.split()
    print(ft_filter.__doc__)
    print(isBigger.__doc__)
    new = list(ft_filter(lambda word: isBigger(word, num), array))
    print(new)


if __name__ == "__main__":
    main()
