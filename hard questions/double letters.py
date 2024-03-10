##def count_pairs(word):
##    for i in range(1, len(word)):
##        print(len(word))
##        amount = 0
##        pair_counter = 0
##        if word[i] == word[i - 1]:
##            if pair_counter < 2:
##                pair_counter += 1
##                amount += 1
##
##        i += 1
##    return amount
##
##
##print(count_pairs('aadvark'))

##def count_pairs(word):
##    for i in range(1, len(word)):
##        amount = 0
##        if word[i] == word[i - 1]:
##           if i != len(word) - 1:
##              if word[i] != word[i + 1]:
##                  amount += 1
##    return amount
##
##word = input('Word: ')
##print(count_pairs(word))
##
##
##def count_adjacent_pairs(word):
##    number_of_adjacent_pairs = 0
##    for index in range(len(word) - 2):
##        first_leter = word[index]
##        second_letter = word[index + 1]
##        third_letter = word[index + 2]
##        if first_letter == second_letter and first_letter != third_letter:
##            number_of_adjacent_pairs += 1
##    return number_of_adjacent_pairs
##
##words = ['aadvark', 'hello', 'computer', 'boook', 'bob', 'hi!!', 'booook', 'Oo', 'heehee']
##for word in words:
##    count = count_adjacent_pairs(word)
##    print(count)

# intro to programming 1#


def a(b):
    p = 0
    e = 0
    f = 0
    for i in range(1, len(word)):
        e = i
        if i < len(word) - 1:
            if b[i] == b[i - 1]:
                while b[e] == b[e + 1]:
                    f += 1
                if f == 0:
                    p += 1
                    e = 0
            f = 0

        else:
            if b[i] == b[i - 1]:
                p += 1
    return p


words = [
    "aadvark",
    "hello",
    "computer",
    "ehdui",
    "jxoeh",
    "boook",
    "hi!!",
    "heehee",
    "Oo",
    "booook",
]

##for word in words:
##    print(word)
##    count = a(word)
##
##    print(word, count)

for word in words:
    print(word)
    count = a(word)
    print(word, count)
