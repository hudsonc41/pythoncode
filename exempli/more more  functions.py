## terms: function, function call, parameter, argument, return value
## placeholder = pass
##
##def area_sqaure(side_length):
##    area = side_length ** 2
##    return area
##
##def main():
##    side = float(input('Side Length of Square: '))
##    area = area_sqaure(side)
##    print(area)

##
##
##def pig_latin(word):
##
##    first_letter = word[0]
##    if first_letter.lower() in ['a', 'e', 'i', 'o', 'u']:
##        return f'{word}ay'
##    else:
##        new_first_letter = word[1].upper()
##        return f'{new_first_letter}{word[2:]}{first_letter.lower()}ay'
##
##
##word = input('word ')
##new_word = pig_latin(word)
##print(new_word)


def pig_latin(word):
    first_letter = word[0]
    if first_letter.lower() in ["a", "e", "i", "o", "u"]:
        return f"{word}ay"
    else:
        new_first_letter = word[1].upper()
        return f"{new_first_letter}{word[2:]}{first_letter.lower()}ay"


# .strip(), .rstrip(), .lstrip()
output = []
words = input("Enter a sentence: ").split()
for word in words:
    output.append(pig_latin(word))
print(" ".join(output))
