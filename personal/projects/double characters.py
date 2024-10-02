import re
def find_adjacent_characters(word):
    pattern = '(\w{2}).*?(\1)'
    pairs = re.findall(pattern, word)
    return pairs

word = input('Enter a word: ')
pairs = find_adjacent_characters(word)
print(pairs)