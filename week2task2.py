#Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.

import re

def simple_function():
    s1 = "Hello7 FH Dortmund 0100 -23"
    digits = []
    total = 0
    for w in s1:
        if w.isdigit():
            digits.append(int(w))

    total = sum(digits)
    print("Sum of all numbers in string s1 = %d " % (sum(digits)))
    print("Average of numbers in string s1 = %f " % ( total/len(digits) ))


def use_regex():

    s1 = "Hello7 FH Dortmund 0100 -23"
    numbers = [int(x) for x in re.findall(r'-?\d+', s1)]

    print(numbers)

    total = sum(numbers)
    print(total)
    avg = total / len(numbers)
    print(avg)

use_regex()
    




    
