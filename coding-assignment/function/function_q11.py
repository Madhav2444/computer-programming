# Question 11: Write a Python function to calculate the area of a circle given its radius.
# Input: circle_area(5)
# Output: 78.54
import math

def circle_area(radius):
    return round(math.pi * radius ** 2, 2)

print(circle_area(5))
