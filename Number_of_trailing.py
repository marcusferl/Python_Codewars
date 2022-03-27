"""
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 * ... * N

Be careful 1000! has 2568 digits...

For more info, see: http://mathworld.wolfram.com/Factorial.html

Examples
zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros
Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.
"""

def zeros(n):
    counter = 0
    result = 1
    for i in range(1,n + 1):
        result = result * i

    result_digits = list(str(result))
    length = len(result_digits)
    while length > 0:
        if int(result_digits[length - 1]) == 0:
            counter +=1
            length -= 1
        else:
            break
    return counter



print(zeros(0))