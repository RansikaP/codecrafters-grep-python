import sys
import re

# import pyparsing - available if you need it!
# import lark - available if you need it!


def match_pattern(input_line, pattern):
    if len(pattern) == 1:
        return pattern in input_line
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")

def match_digits(input_line):
    if re.search("[0-9]", input_line):
        print('2')
        return 0
    else:
        print('3')
        return 1


def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    if pattern == '\d':
        print('here')
        exit(match_digits(input_line))
    elif match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)


if __name__ == "__main__":
    main()
