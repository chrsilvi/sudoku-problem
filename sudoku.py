combinations = {}
for x in range(10):
    combinations[x+1] = []
# examples of what the dictionary of results will look like:
# combinations[1] = [1]
# combinations[3] = [2, 1]
# combinations[5] = [[4, 1], [3, 2]]
digits = [1, 2, 3, 4]

# this goes through up to 3 digits, trying to figure out how to formulate
# this to go through anywhere from 1-9 digits
# need to use recursion somehow in the bowels of this function

variable_list = []

def verify_combination(variable_list, combinations):
    this_total = 0
    for x in range(len(variable_list)):
        this_total += variable_list[x]
    combinations[this_total] += variable_list


def inception(digits, combinations):
    global variable_list
    for x in range(len(digits)):
        this_iteration = digits[x]
        this_iteration = digits[x]
        variable_list.append(this_iteration)
        digits.remove(this_iteration)
        print(variable_list)
        verify_combination(variable_list, combinations)
        inception(digits, combinations)
        variable_list.remove(this_iteration)
        digits.append(this_iteration)
        digits.sort()


def variables():
    global master_digits
    global digits
    global combinations
    inception(digits, combinations)


variables()
for x in range(len(combinations)):
    print("The possible combinations for " + str(x+1) + " are:")
    print(combinations[x+1])
    print("\n")
