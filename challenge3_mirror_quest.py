# def find_longest_mirror_length(s):
#     def solve(left, right):
#         if left > right:
#             return 0
#         if left == right:
#             return 1

#         if s[left] == s[right]:
#             return 2 + solve(left + 1, right - 1)
#         else:
#             return max(
#                 solve(left + 1, right),
#                 solve(left, right - 1)
#             )

#     return solve(0, len(s) - 1)


# # Example
# print(find_longest_mirror_length("bbabcbcab"))


def find_longest_mirror_length(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # Single characters are palindromes
    for i in range(n):
        dp[i][i] = 1

    # Build for increasing substring lengths
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = 2 + (dp[i + 1][j - 1] if length > 2 else 0)
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


# Example
print(find_longest_mirror_length("bbabcbcab"))
