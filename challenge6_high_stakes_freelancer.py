def maximize_freelance_profit(deadlines, profits):
    jobs = list(zip(deadlines, profits))
    n = len(jobs)
    max_profit = 0
    max_jobs = 0

    def backtrack(index, time, profit, count):
        nonlocal max_profit, max_jobs

        if index == n:
            if profit > max_profit:
                max_profit = profit
                max_jobs = count
            return

        # Skip job
        backtrack(index + 1, time, profit, count)

        # Take job if it fits
        if time + 1 <= jobs[index][0]:
            backtrack(index + 1, time + 1, profit + jobs[index][1], count + 1)

    backtrack(0, 0, 0, 0)
    return [max_jobs, max_profit]

