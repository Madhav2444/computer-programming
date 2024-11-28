# Question 13: Write a Python program to find the last occurrence of a substring in a string.
# Input: "hello world", "o"
# Output: 7
string = "hello world"
last_index = string.rfind("o")
print("Index of last occurrence of 'o':", last_index)
