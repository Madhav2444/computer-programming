# Question 1: Write a Python program to merge two dictionaries.
# Input: dict1 = {'a': 1, 'b': 2}, dict2 = {'c': 3, 'd': 4}
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}
print("Merged Dictionary:", merged_dict)