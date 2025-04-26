def sum_digits(number):
    remainder=number%10
    if number//10==0:
        return remainder
    return remainder+sum_digits(number//10)
print(sum_digits(782))