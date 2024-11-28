# Question 19: Write a Python program to find the intersection of two lists.
# Input: [1, 2, 3] and [2, 3, 4]
# Output: [2, 3]
list1 = [1, 2, 3]
list2 = [2, 3, 4]
intersection = list(set(list1) & set(list2))
print("Intersection:", intersection)
