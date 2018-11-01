import sys
# This became really gross, but at least I did it differently.
opener_list = ['(', '[', '{', '<', '(*']
closer_list = [')', ']', '}', '>', '*)']


def read_file(filename):
    with open(filename) as f:
        for string in f:
            bracket_check(string.strip())


def bracket_check(string):
    stack = []
    for i, char in enumerate(string):
        if char in opener_list:
            double_token = string[i: i+2]
            if double_token == "(*":
                stack.append(double_token)
            else:
                stack.append(char)
        elif char in closer_list:
            opener_index = closer_list.index(char)
            opener_token = opener_list[opener_index]
            cl_double_token = string[i-1: (i+1)]
            cl_dbl_tkn_check = string[(i-2): (i)]
            find_opener_ind = string[0:(i-1)]
            if cl_double_token == "*)" and "(*" in find_opener_ind:
                if cl_dbl_tkn_check != "(*" and double_token == "(*":
                        stack.pop()
            elif stack[-1] == opener_token:
                stack.pop()
            elif not stack or opener_token not in stack:
                print ("No. Unbalanced. Closer with no previous opener.")
                break
            else:
                pass
    if stack or i < len(string)-1:
        print("=============================================================")
        print stack
        print("No, it's unbalanced!")
        print("=============================================================")

    else:
        print("=============================================================")
        print stack
        print("Yes! It's balanced!")
        print("=============================================================")


def main():
    if len(sys.argv) != 2:
        print 'usage: python brackets.py file-to-read'
        sys.exit(1)
    filename = sys.argv[1]
    if filename:
        read_file(filename)


if __name__ == '__main__':
    main()
