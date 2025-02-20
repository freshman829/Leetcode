class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        mask = 0

        for digit in nums:
            mask |= 1 << digit.count("1")
        n = len(nums)

        for i in range(n + 1):
            if mask >> i & 1 ^ 1:
                return "1" * i + "0" * (n - i)