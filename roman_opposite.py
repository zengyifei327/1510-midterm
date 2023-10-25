"""

"""


def roman_to_int(roman_numeral):
    roman_numerals = {
        'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
        'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
        'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
    }

    result = 0
    i = 0

    while i < len(roman_numeral):
        if i + 1 < len(roman_numeral) and roman_numeral[i:i + 2] in roman_numerals:  # slice, i + 2 exclusive
            result += roman_numerals[roman_numeral[i:i + 2]]
            i += 2
        else:
            result += roman_numerals[roman_numeral[i]]
            i += 1

    return result


def main():
    roman_numeral = "MMXXIII"  # Roman numeral for 2023
    integer_value = roman_to_int(roman_numeral)
    print(f"The integer value of {roman_numeral} is {integer_value}")

    roman_numeral = "CMXL"  # Roman numeral for 940
    integer_value = roman_to_int(roman_numeral)
    print(f"The integer value of {roman_numeral} is {integer_value}")


if __name__ == "__main__":
    main()
