# Question 18: Write a Python program to rotate a list to the left by n positions.
# Input: [1, 2, 3, 4, 5], n=2
# Output: [3, 4, 5, 1, 2]
numbers = [1, 2, 3, 4, 5]
n = 2
rotated_list = numbers[n:] + numbers[:n]
print("Rotated list:", rotated_list)
