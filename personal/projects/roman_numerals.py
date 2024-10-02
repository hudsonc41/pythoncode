roman_numerals = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

roman_number = input("Roman number: ")


def convert(roman_number):
    roman_characters = list(roman_number)
    hindu_number = 0
    for position, character in enumerate(roman_characters):
        if character in roman_numerals:
            if position != len(roman_characters) - 1:
                next_character = roman_characters[position + 1]
                if roman_numerals[character] < roman_numerals[next_character]:
                    hindu_number -= roman_numerals[character]
                else:
                    hindu_number += roman_numerals[character]
            else:
                hindu_number += roman_numerals[character]
        else:
            return "Not a valid Roman numeral."
            exit()
    return hindu_number


hindu_number = convert(roman_number)
print(f"The corresponding Hindu-Arabic number is {hindu_number}.")

test_cases = [
    "I",
    "II",
    "III",
    "IV",
    "V",
    "XLIV",
    "XXXVII",
    "CI",
    "IC",
    "XCIX",
    "CMLXVI",
    "MDCI",
]
test_sols = [1, 2, 3, 4, 5, 44, 37, 101, 99, 99, 966, 1601]
for index, test in enumerate(test_cases):
    test_cases[index] = convert(test)

if test_cases == test_sols:
    print("Successful.")
else:
    for index, test in enumerate(test_cases):
        if test != test_sols[index]:
            print(f"Wrong submission at {index}")
            print(test, test_sols[index])
