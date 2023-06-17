class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        max_len = 1
        start = 0

        # Single characters are palindromes
        for i in range(n):
            dp[i][i] = True

        # Check for palindromes of length 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                max_len = 2
                start = i

        # Check for palindromes of length > 2
        for k in range(3, n+1):
            for i in range(n-k+1):
                j = i + k - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if k > max_len:
                        max_len = k
                        start = i

        return s[start:start+max_len]