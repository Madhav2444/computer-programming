# Question 2: Write a Python program to find the value associated with a given key in a dictionary.
# Input: dict = {'a': 1, 'b': 2, 'c': 3}, key = 'b'
# Output: 2
dict = {'a': 1, 'b': 2, 'c': 3}
key = 'b'
value = dict.get(key, "Key not found")
print("Value for key:", value)
