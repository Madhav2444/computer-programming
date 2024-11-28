# Question 15: Write a Python program to count the number of vowels in a string.
# Input: "hello"
# Output: 2
string = "hello"
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in string if char in vowels)
print("Number of vowels:", vowel_count)
