# Question 2: Write a Python function to calculate the factorial of a number.
# Input: factorial(5)
# Output: 120
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
