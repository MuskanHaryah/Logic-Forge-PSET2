# def count_payment_combinations(coins, total_sum):
#     def solve(index, remaining):
#         # Exact payment made
#         if remaining == 0:
#             return 1

#         # Invalid path
#         if remaining < 0 or index == len(coins):
#             return 0

#         # Include current coin OR skip it
#         include = solve(index, remaining - coins[index])
#         exclude = solve(index + 1, remaining)

#         return include + exclude

#     return solve(0, total_sum)


# # Example
# print(count_payment_combinations([1, 2, 3], 4))


def count_payment_combinations(coins, total_sum):
    dp = [0] * (total_sum + 1)
    dp[0] = 1  # One way to make sum 0

    for coin in coins:
        for s in range(coin, total_sum + 1):
            dp[s] += dp[s - coin]

    return dp[total_sum]


# Example
print(count_payment_combinations([2, 5, 3, 6], 10))
