# Question 5: Write a Python program to check if a key exists in a dictionary.
# Input: dict = {'a': 1, 'b': 2, 'c': 3}, key = 'b'
# Output: True
dict = {'a': 1, 'b': 2, 'c': 3}
key_to_check = 'b'
exists = key_to_check in dict
print("Key exists:", exists)
