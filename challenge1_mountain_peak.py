def count_ways_to_summit(n):
    # Base cases
    if n == 0 or n == 1:
        return 1

    # Recursive exploration
    return count_ways_to_summit(n - 1) + count_ways_to_summit(n - 2)


# Example
print(count_ways_to_summit(5))
