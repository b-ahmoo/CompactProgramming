def factorial(number):
    if (number != 1):
        return number * factorial(number-1)
    else:
        return number

result = factorial(5)
print(result)