class Solution(object):
    def constructDistancedSequence(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def backtrack(i):
            if i == 2 * n:
                return True
            if sequence[i]:
                return backtrack(i + 1)
            for num in range(n, 1, -1):
                if cnt[num] and i + num < n * 2 and sequence[i + num] == 0:
                    cnt[num] = 0
                    sequence[i] = sequence[i + num] = num
                    if backtrack(i + 1):
                        return True
                    sequence[i] = sequence[i + num] = 0
                    cnt[num] = 2
            if cnt[1]:
                cnt[1] = 0
                sequence[i] = 1
                if backtrack(i + 1):
                    return True
                sequence[i] = 0
                cnt[1] = 1
            return False

        sequence = [0] * (n * 2)
        cnt = [2] * (n * 2)
        cnt[1] = 1
        backtrack(1)
        return sequence[1:]

        