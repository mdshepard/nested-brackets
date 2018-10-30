import sys


def bracket_check(filename):
    with open(filename) as f:
        text = [line for line in f]
        print "some text"
        print text
        print "that was some text"
    pairs = {
        "(": ")",
        "{": "}",      # matching keys,values to determine if a bracket is
                       # complete or not
        "<": ">",
        "[": "]",
        "(*": "*)"
    }
    opened_bracks = pairs.keys()  # get the opening brackets
    closed_bracks = pairs.values()  # get the closing brackets
    brackets = opened_bracks + closed_bracks

    tokens = []
    to_be_closed = []

    for char in text:
        token = text.pop(0)
        if text and (token == "(" and text[0] == "*" or token == "*"
                     and text[0] == ")"):
            token += text.pop(0)

        tokens.append(token)

        if token not in brackets:
            continue
        if token in opened_bracks:
            to_be_closed.append(token)
        elif token in closed_bracks:
            opened = to_be_closed[-1]
            if token == pairs[opened]:
                to_be_closed.pop()
            else:
                tokens.pop()
                break

    if not to_be_closed:
        print("Yep")
        return "YES"
    else:
        print("Nope")
        return "NO {}".format(len(tokens)+1)


def main():
    if len(sys.argv) != 2:
        print 'usage: python brackets.py file-to-read'
        sys.exit(1)
    filename = sys.argv[1]
    if filename:
        bracket_check(filename)


if __name__ == '__main__':
    main()
