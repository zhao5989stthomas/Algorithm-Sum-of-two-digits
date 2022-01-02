# python3 
#Sum of Two Digits


def sum_of_two_digits(first_digit, second_digit):
    sum = first_digit + second_digit
    return sum

if __name__ == '__main__':
    a=int(input("Enter the first number:")) 
    b=int(input("Enter the sencond number:"))
    print("Sum of two digits:" + str(sum_of_two_digits(a, b)))

