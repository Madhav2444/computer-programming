# Question 13: Write a Python function to check if a list is sorted.
# Input: is_sorted([1, 2, 3, 4])
# Output: True
def is_sorted(lst):
    return lst == sorted(lst)

print(is_sorted([1, 2, 3, 4]))
