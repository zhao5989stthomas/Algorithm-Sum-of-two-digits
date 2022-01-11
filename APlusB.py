# python3

def sum_of_two_digits(first_digit, second_digit):
    return first_digit + second_digit

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(sum_of_two_digits(a, b))

# a, b = map(int, input().split())
# input() will query the user for input, and read one line of user input;
# split() will split that input into a list of "words";
# map(int, ...) will call int on each word, it will to that lazily (although that is not important here); and
# a, b = ... will unpack the expression into two elements, and assign the first one to n and the second one to S.
