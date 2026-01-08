# def calculate_minimum_speed(piles, k):
#     max_pile = max(piles)

#     for s in range(1, max_pile + 1):
#         hours = 0
#         for pile in piles:
#             hours += (pile + s - 1) // s  # ceiling division

#         if hours <= k:
#             return s


def calculate_minimum_speed(piles, k):
    left, right = 1, max(piles)
    answer = right

    while left <= right:
        mid = (left + right) // 2
        hours = 0

        for pile in piles:
            hours += (pile + mid - 1) // mid

        if hours <= k:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


# Examples
print(calculate_minimum_speed([5, 10, 3], 4))        # 5
print(calculate_minimum_speed([5, 10, 15, 20], 7))  # 10
