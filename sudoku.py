combinations = {}
# combinations[1] = [1]
# combinations[3] = [2, 1]
# combinations[5] = [[4, 1], [3, 2]]
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# def function(variables, sum):
#     for x in range(variables):

def calculate():
    for sums in range(18):
        combinations[sums] = []
        for x in range(len(digits)):
            for y in range(len(digits)):
                if digits[x] + digits[y] == sums and digits[x] != digits[y]:
                    newCombo = [digits[x], digits[y]]
                    newCombo.sort()
                    if newCombo not in combinations[sums]:
                        combinations[sums] += [newCombo]
                for z in range(len(digits)):
                    if digits[x] + digits[y] + digits[z] == sums and digits[x] != digits[y] and digits[y] != digits[z] and digits[x] != digits[z]:
                        newCombo = [digits[x], digits[y], digits[z]]
                        newCombo.sort()
                        if newCombo not in combinations[sums]:
                            combinations[sums] += [newCombo]

def combinations(integers, sum):
    total = 0
    for x in range(integers):
        total += integers[x]
    if total == sum:
        return true


calculate()
for x, y in combinations.items():
    print(x, y)
