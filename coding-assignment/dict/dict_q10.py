# Question 10: Write a Python program to create a dictionary from two lists.
# Input: keys = ['a', 'b', 'c'], values = [1, 2, 3]
# Output: {'a': 1, 'b': 2, 'c': 3}
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = dict(zip(keys, values))
print("Dictionary from lists:", dictionary)
