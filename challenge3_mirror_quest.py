def find_longest_mirror_length(s):
    def solve(left, right):
        if left > right:
            return 0
        if left == right:
            return 1

        if s[left] == s[right]:
            return 2 + solve(left + 1, right - 1)
        else:
            return max(
                solve(left + 1, right),
                solve(left, right - 1)
            )

    return solve(0, len(s) - 1)


# Example
print(find_longest_mirror_length("bbabcbcab"))
