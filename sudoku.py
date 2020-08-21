combinations = {}
# examples of what the dictionary of results will look like:
# combinations[1] = [1]
# combinations[3] = [2, 1]
# combinations[5] = [[4, 1], [3, 2]]
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# this goes through up to 3 digits, trying to figure out how to formulate
# this to go through anywhere from 1-9 digits
# need to use recursion somehow in the bowels of this function

variable_list = []
current_sum = 1
def variables():
    global current_sum
    global digits
    while current_sum < 46:
        for x in range(len(digits)):
            variable_list.append(digits[x])
            digits.remove(digits[x])
            verify_combination(variable_list, current_sum)
            print(current_sum)
            print(variable_list)
            current_sum += 1
            for y in range(len(digits)):
                variable_list.append(digits[y])
                print(variable_list)
                variable_list.remove(digits[y])
            digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            variable_list.remove(digits[x])

    #cycle through and provide every combination of variables

def verify_combination(variable_list, current_sum):
    pass
    #double check if that combination of variables equals the sum
    #adds it to combinations if so

variables();
