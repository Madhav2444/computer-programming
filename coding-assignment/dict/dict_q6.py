# Question 6: Write a Python program to iterate over the keys and values of a dictionary.
# Input: dict = {'a': 1, 'b': 2, 'c': 3}
# Output: a: 1, b: 2, c: 3
dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in dict.items():
    print(f"{key}: {value}")
