class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def backtrack(t):
            if len(t) == n:
                arr.append(t)
                return
            for char in "abc":
                if t and t[-1] == char:
                    continue
                backtrack(t + char)

        arr = []
        backtrack("")

        return '' if len(arr) < k else arr[k - 1]