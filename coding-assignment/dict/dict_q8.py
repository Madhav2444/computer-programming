# Question 8: Write a Python program to add a key-value pair to a dictionary.
# Input: dict = {'a': 1, 'b': 2}, key = 'c', value = 3
# Output: {'a': 1, 'b': 2, 'c': 3}
dict = {'a': 1, 'b': 2}
new_key = 'c'
new_value = 3
dict[new_key] = new_value
print("Updated Dictionary:", dict)
