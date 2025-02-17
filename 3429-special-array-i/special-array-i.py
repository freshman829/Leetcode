class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(1, len(nums)):
            if not ((nums[i] ^ nums[i-1]) & 1):
                return False
        return True  
            