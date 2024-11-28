# Question 8: Write a Python function to find the Fibonacci sequence up to n terms.
# Input: fibonacci(5)
# Output: [0, 1, 1, 2, 3]
def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence[:n]

print(fibonacci(5))
