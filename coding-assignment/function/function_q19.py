# Question 19: Write a Python function to count the frequency of each character in a string.
# Input: char_frequency("hello")
# Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
def char_frequency(s):
    return {char: s.count(char) for char in set(s)}

print(char_frequency("hello"))
