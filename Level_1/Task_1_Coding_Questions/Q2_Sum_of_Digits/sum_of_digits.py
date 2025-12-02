# Task 2 - Sum of Digits
# This program calculates the sum of digits of a number.

number = 123

def sum_of_digits(num):

    # Convert number to string to iterate through digits
    num = str(num)
    total = 0

    # Add each digit to the total
    for digit in num:
        total += int(digit)

    return total

print("Sum of Digits:", sum_of_digits(number))
