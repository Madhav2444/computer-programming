# Question 3: Write a Python program to remove a key from a dictionary.
# Input: dict = {'a': 1, 'b': 2, 'c': 3}, key = 'b'
# Output: {'a': 1, 'c': 3}
dict = {'a': 1, 'b': 2, 'c': 3}
key_to_remove = 'b'
dict.pop(key_to_remove, None)
print("Dictionary after removal:", dict)
