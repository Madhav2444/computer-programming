# Question 4: Write a Python function to check if a string is a palindrome.
# Input: is_palindrome("radar")
# Output: True
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar"))
