class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        maxLen = 0
        zerosCount = 0

        while right < len(nums):
            if nums[right] == 0:
                zerosCount += 1

            while zerosCount > 1:
                if nums[left] == 0:
                    zerosCount -= 1
                left += 1

            maxLen = max(maxLen, right - left)

            right += 1

        return maxLen