#!/usr/bin/python3

def roman_to_int(roman_string):
    if isinstance(roman_string, str):
        roman_numerals = {
                'M': 1000,
                'CM': 900,
                'D': 500,
                'CD': 400,
                'C': 100,
                'XC': 90,
                'L': 50,
                'XL': 40,
                'X': 10,
                'IX': 9,
                'V': 5,
                'IV': 4,
                'I': 1
        }
        i = 0
        x = 0
        while (i < len(roman_string)):
            if (i + 1 < len(roman_string) and roman_string[i:i+2] in
                    roman_numerals):
                x += roman_numerals[roman_string[i:i+2]]
                i += 2
            else:
                x += roman_numerals[roman_string[i]]
                i += 1
        return x
