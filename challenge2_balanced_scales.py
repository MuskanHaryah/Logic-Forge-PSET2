def can_balance_scales(arr):
    total = sum(arr)

    # If total weight is odd, cannot split
    if total % 2 != 0:
        return False

    target = total // 2

    def helper(index, current_sum):
        # Found valid subset
        if current_sum == target:
            return True

        # Out of bounds or sum exceeded
        if index == len(arr) or current_sum > target:
            return False

        # Choice: take or skip current stone
        return (
            helper(index + 1, current_sum + arr[index]) or
            helper(index + 1, current_sum)
        )

    return helper(0, 0)


# Example
print(can_balance_scales([1, 5, 11, 5]))
