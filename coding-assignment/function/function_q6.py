# Question 6: Write a Python function to count the vowels in a string.
# Input: count_vowels("hello")
# Output: 2
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

print(count_vowels("hello"))
