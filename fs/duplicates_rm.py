lists = [1, 3, 2, 6, 4, 4, 5, 8, 2]
uniques = []
for number in lists:
    if number not in uniques:
        uniques.append(number)
        uniques.sort()

print(uniques)
