#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    string = roman_string
    numbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in string:
        if i not in numbers or roman_string is None:
            return 0
        elif type(roman_string) != str:
            return 0
    # if the number is less than the next subtract it from the num
    for i in range(len(string)):
        if i != len(string) - 1:
            if numbers[string[i]] < numbers[string[i+1]]:
                num -= numbers[string[i]]
            else:
                num += numbers[string[i]]
        else:
            num += numbers[string[i]]
    return num
