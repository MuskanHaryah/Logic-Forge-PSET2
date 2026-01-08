# def min_cancelled_bookings(intervals):
#     intervals.sort()

#     def has_overlap(schedule):
#         for i in range(1, len(schedule)):
#             if schedule[i][0] < schedule[i - 1][1]:
#                 return True
#         return False

#     n = len(intervals)
#     min_removed = n

#     def backtrack(index, chosen):
#         nonlocal min_removed

#         if has_overlap(chosen):
#             return

#         min_removed = min(min_removed, n - len(chosen))

#         for i in range(index, n):
#             backtrack(i + 1, chosen + [intervals[i]])

#     backtrack(0, [])
#     return min_removed

def min_cancelled_bookings(intervals):
    if not intervals:
        return 0

    # Sort by end time
    intervals.sort(key=lambda x: x[1])

    removals = 0
    last_end = intervals[0][1]

    for i in range(1, len(intervals)):
        start, end = intervals[i]

        if start < last_end:
            # Overlap found → cancel this booking
            removals += 1
        else:
            last_end = end

    return removals


# Examples
print(min_cancelled_bookings([[1, 2], [2, 3], [3, 4], [1, 3]]))  # 1
print(min_cancelled_bookings([[1, 3], [1, 3], [1, 3]]))        # 2
print(min_cancelled_bookings([[1, 2], [5, 10], [18, 35]]))     # 0
