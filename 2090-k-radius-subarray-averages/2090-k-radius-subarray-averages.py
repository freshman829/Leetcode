class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        avgs = [-1] * n
        
        if n <= 2*k:
            return avgs
        # Calculate the sum of the first 2k+1 elements
        total = sum(nums[:2 * k + 1])
        avgs[k] = total // (2 * k + 1)

        # Calculate the sum of each subarray of size 2k+1 centered at index i
        for i in range(k + 1, n-k):
            total += nums[i+k]
            total -= nums[i-k-1]
            avgs[i] = total // (2*k+1)

        # Fill in the remaining elements with the last valid average
        for i in range(n-k, n):
            avgs[i] = -1

        return avgs
        