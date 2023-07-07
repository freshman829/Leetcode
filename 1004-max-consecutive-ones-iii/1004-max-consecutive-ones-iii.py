class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length = 0
        max_count = 0
        start = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                k -= 1

            while k < 0:
                if nums[start] == 0:
                    k += 1
                start += 1

            max_length = max(max_length, end - start + 1)
            max_count = max(max_count, max_length)

        return max_count