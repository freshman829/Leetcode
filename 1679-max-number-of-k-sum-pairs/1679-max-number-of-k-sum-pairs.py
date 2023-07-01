class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        num_count = {}

        for num in nums:
            if num in num_count and num_count[num] > 0:
                count += 1
                num_count[num] -= 1
            else:
                complement = k - num
                num_count[complement] = num_count.get(complement, 0) + 1

        return count