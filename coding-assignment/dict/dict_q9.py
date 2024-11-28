# Question 9: Write a Python program to sort a dictionary by its keys.
# Input: {'b': 2, 'c': 3, 'a': 1}
# Output: {'a': 1, 'b': 2, 'c': 3}
dict = {'b': 2, 'c': 3, 'a': 1}
sorted_dict = dict(sorted(dict.items()))
print("Sorted Dictionary by keys:", sorted_dict)
