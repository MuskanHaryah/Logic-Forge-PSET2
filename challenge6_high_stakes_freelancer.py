# def maximize_freelance_profit(deadlines, profits):
#     jobs = list(zip(deadlines, profits))
#     n = len(jobs)
#     max_profit = 0
#     max_jobs = 0

#     def backtrack(index, time, profit, count):
#         nonlocal max_profit, max_jobs

#         if index == n:
#             if profit > max_profit:
#                 max_profit = profit
#                 max_jobs = count
#             return

#         # Skip job
#         backtrack(index + 1, time, profit, count)

#         # Take job if it fits
#         if time + 1 <= jobs[index][0]:
#             backtrack(index + 1, time + 1, profit + jobs[index][1], count + 1)

#     backtrack(0, 0, 0, 0)
#     return [max_jobs, max_profit]


def maximize_freelance_profit(deadlines, profits):
    jobs = sorted(zip(deadlines, profits), key=lambda x: x[1], reverse=True)
    max_deadline = max(deadlines)

    parent = list(range(max_deadline + 1))

    def find(slot):
        if parent[slot] != slot:
            parent[slot] = find(parent[slot])
        return parent[slot]

    def union(u, v):
        parent[v] = u

    total_profit = 0
    jobs_done = 0

    for deadline, profit in jobs:
        available_slot = find(deadline)
        if available_slot > 0:
            union(find(available_slot - 1), available_slot)
            total_profit += profit
            jobs_done += 1

    return [jobs_done, total_profit]


# Example
print(maximize_freelance_profit(
    deadlines=[2, 1, 2, 1, 3],
    profits=[100, 19, 27, 25, 15]
))
