class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        length = len(nums)
        max_len = 0
        cur_len = 0
        for i in range(length):
            if i == 0:
                cur_len += 1
                continue
            if nums[i] > nums[i - 1]:
                cur_len += 1
            else:
                max_len = max(cur_len, max_len)
                cur_len = 1
        max_len = max(cur_len, max_len)
        return max_len
            