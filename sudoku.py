combinations = {}
# examples of what the dictionary of results will look like:
# combinations[1] = [1]
# combinations[3] = [2, 1]
# combinations[5] = [[4, 1], [3, 2]]
digits = [1, 2, 3, 4]

# this goes through up to 3 digits, trying to figure out how to formulate
# this to go through anywhere from 1-9 digits
# need to use recursion somehow in the bowels of this function

variable_list = []
current_sum = 3


def verify_combination(variable_list, current_sum):
    this_total = 0
    for x in range(len(variable_list)):
        this_total += variable_list[x]
    if this_total == current_sum:
        combinations[current_sum] = variable_list


def inception(digits, current_sum):
    global variable_list
    for x in range(len(digits)):
        this_iteration = digits[x]
        this_iteration = digits[x]
        variable_list.append(this_iteration)
        digits.remove(this_iteration)
        print(variable_list)
        verify_combination(variable_list, current_sum)
        inception(digits, current_sum)
        variable_list.remove(this_iteration)
        digits.append(this_iteration)
        digits.sort()


def variables():
    global current_sum
    global master_digits
    global digits
    print(current_sum)
    inception(digits, current_sum)


variables()
print(combinations)
