# Question 4: Write a Python program to count the frequency of each character in a string using a dictionary.
# Input: "hello"
# Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
string = "hello"
frequency = {}
for char in string:
    frequency[char] = frequency.get(char, 0) + 1
print("Character frequency:", frequency)
