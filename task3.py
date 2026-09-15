def factorial(number):
    if (number != 1):
        return number * factorial(number-1)
    else:
        return number

def variable_conversion():
    number = 9
    print("Integer to float = ", float(number))

    fp = 9.789
    print("Floating point to integer = ", int(fp))

    print ("Integer to string = "+ str(number))

    stringWithNumber = "4"
    bool_variable = 0
    print("Converting string with a number to integer = ", (stringWithNumber))
    print("Converting integer to boolean = ", bool(bool_variable))

# print(factorial(6))

variable_conversion()
