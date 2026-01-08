# def count_ways_to_summit(n):
#     # Base cases
#     if n == 0 or n == 1:
#         return 1

#     # Recursive exploration
#     return count_ways_to_summit(n - 1) + count_ways_to_summit(n - 2)


# # Example
# print(count_ways_to_summit(5))

def count_ways_to_summit(n):
    if n == 0 or n == 1:
        return 1

    prev2 = 1  # ways to reach step 0
    prev1 = 1  # ways to reach step 1

    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1


# Example
print(count_ways_to_summit(45))
