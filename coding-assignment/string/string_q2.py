# Question 2: Write a Python program to check if a string is a palindrome.
# Input: "radar"
# Output: True
string = "radar"
is_palindrome = string == string[::-1]
print("Is palindrome:", is_palindrome)
