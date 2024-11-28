# Question 16: Write a Python program to reverse the order of words in a string.
# Input: "Python is fun"
# Output: "fun is Python"
string = "Python is fun"
reversed_words = " ".join(string.split()[::-1])
print("Reversed words:", reversed_words)
