"""

"""


def int_to_roman(input_number):
    roman_numerals = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }
    if input_number < 0 or input_number > 5000:
        return "Invalid input"

    roman_numeral = ""
    for value, numeral in roman_numerals.items():
        while input_number >= value:
            roman_numeral += numeral
            input_number -= value

    return roman_numeral


def main():
    print(int_to_roman(4999))
    print(int_to_roman(-1))
    print(int_to_roman(6000))


if __name__ == "__main__":
    main()
