def min_cancelled_bookings(intervals):
    intervals.sort()

    def has_overlap(schedule):
        for i in range(1, len(schedule)):
            if schedule[i][0] < schedule[i - 1][1]:
                return True
        return False

    n = len(intervals)
    min_removed = n

    def backtrack(index, chosen):
        nonlocal min_removed

        if has_overlap(chosen):
            return

        min_removed = min(min_removed, n - len(chosen))

        for i in range(index, n):
            backtrack(i + 1, chosen + [intervals[i]])

    backtrack(0, [])
    return min_removed
