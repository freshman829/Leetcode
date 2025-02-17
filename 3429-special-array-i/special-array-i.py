class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True
        
        step = 1
        def parity(num):
            if num % 2 == 1:
                return False
            else:
                return True

        while step < len(nums):
            if parity(nums[step]) == parity(nums[step - 1]):
                return False
            step += 1
        
        return True
            