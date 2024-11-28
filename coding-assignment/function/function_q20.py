# Question 20: Write a Python function to flatten a nested list.
# Input: flatten_list([[1, 2], [3, 4], [5]])
# Output: [1, 2, 3, 4, 5]
def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

print(flatten_list([[1, 2], [3, 4], [5]]))
