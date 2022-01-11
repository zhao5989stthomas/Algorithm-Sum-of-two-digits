# python3
#Sum of Two Digits

def sum_of_two_digits(first_digit, second_digit):
    sum = first_digit + second_digit
    return sum    

if __name__ == '__main__':
    inp = input("Please enter two digits separated by space: ").split()
    a = int(inp[0])
    b = int(inp[1])
    print (sum_of_two_digits(a, b))
