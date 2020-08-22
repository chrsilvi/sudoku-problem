# combinations = {}
# combinations[1] = [1]
# combinations[3] = [2, 1]
# combinations[5] = [[4, 1], [3, 2]]
# combinations[9] = []
#
# variable_list = [2, 3, 4]
# this_total = 0
# for x in range(len(variable_list)):
#     this_total += variable_list[x]
# print(this_total)
# combinations[this_total] += variable_list
# combinations[9] += [2, 3]
# print(combinations)
#
# def verify_combination(variable_list, combinations):
#     this_total = 0
#     for x in range(len(variable_list)):
#         this_total += variable_list[x]
#     combinations[this_total] += [variable_list]

nested_list = {}
nested_list[0] = []
new_list = [2, 1]
nested_list[0] += [new_list]
print(nested_list)
