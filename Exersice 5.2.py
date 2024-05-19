list = [2, 2, 3, 3, 4]
current_average = sum(list) / len(list)
number_to_add = 5 * (len(list) + 1) - sum(list)
list.append(number_to_add)
print("Updated list:", list)