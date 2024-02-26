sentence = "This is a common interview question"
occurences = {}

for chr in sentence:
    occurences[chr.lower()] = sentence.count(chr.lower())

occ = tuple(occurences.values())
max_occurence = max(occ)
for character in occurences:
    if occurences[character] == max_occurence:
        print(f"{character} has appeared the most with {max_occurence} occurrences")


# def totalBits(n):
#     bits = DecimalToBinary(n)
#     return bits.count("1")


# def DecimalToBinary(n):
#     if n // 2 == 0:
#         return str(n % 2)
#     return DecimalToBinary(n // 2) + str(n % 2)


# print(totalBits(7))
