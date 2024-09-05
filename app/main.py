import sys
import re

# import pyparsing - available if you need it!
# import lark - available if you need it!


def match_pattern(input_line, pattern):
    if len(pattern) == 1:
        return pattern in input_line
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")

def match_d_an_cg(input, pattern):
    return 0 if re.search (pattern, input) else 1

def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    print('pattern: ', pattern)
    print('input_line: ', input_line)

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    if pattern.count('\\') > 1:
        for c in pattern:
            if c == '\\':
                print(c.next())
    elif pattern.startswith('\\') or re.search("^\[.*\]$", pattern):
        exit(match_d_an_cg(input_line, pattern))
    elif match_pattern(input_line, pattern):
        exit(0)
    
    exit(1)


if __name__ == "__main__":
    main()
