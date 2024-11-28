# Question 17: Write a Python program to flatten a nested list.
# Input: [[1, 2], [3, 4], [5]]
# Output: [1, 2, 3, 4, 5]
nested_list = [[1, 2], [3, 4], [5]]
flattened_list = [item for sublist in nested_list for item in sublist]
print("Flattened list:", flattened_list)
