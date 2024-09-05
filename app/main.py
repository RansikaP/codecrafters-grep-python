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

def combined_char(input, pattern):
    patterns = pattern.split(' ')
    for p in patterns:
        if not re.search(p, input):
            return 1
    
    return 0

def backreference(input, pattern):
    patterns = pattern.split(')')
    ref = patterns[0][1:]
    count = re.findall(r'\\\d+', pattern)[0]
    count = count[1:]

    pattern_split = pattern.split(',')
    input_split = input.split(',')
    if pattern_split[1] != input_split[0]
        return 1

    matches = re.findall(ref, input)
    print(matches)
    if int(count) + 1 == len(matches):
        return 0
    else: return 1
    
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
    if pattern.startswith('('):
        exit(backreference(input_line, pattern))
    elif pattern.count('\\') > 1:
        exit(combined_char(input_line, pattern))
    else:
        exit(match_d_an_cg(input_line, pattern))
    
    exit(1)


if __name__ == "__main__":
    main()
