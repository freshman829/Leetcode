class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero = filter(lambda num: num != 0, nums)
        length = len(list(non_zero))
        if length == 0:
            return
        step = 0
        while step < len(nums):
            if nums[step] == 0:
                nums.pop(step)
                nums.append(0)
            else:
                step += 1
            if step == length:
                break
            
        