def calculate_minimum_speed(piles, k):
    max_pile = max(piles)

    for s in range(1, max_pile + 1):
        hours = 0
        for pile in piles:
            hours += (pile + s - 1) // s  # ceiling division

        if hours <= k:
            return s
