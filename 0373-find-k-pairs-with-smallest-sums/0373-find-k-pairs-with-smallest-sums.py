class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        result = []

        # create heap with first min(k, len(nums1)*len(nums2)) elements
        for i in range(min(k, len(nums1))):
            heap.append([nums1[i]+nums2[0], i, 0])
        heapify(heap)

        # pop smallest element from heap k times
        for _ in range(min(k, len(nums1)*len(nums2))): 
            if not heap:
                break
            s, i, j = heappop(heap)
            result.append([nums1[i], nums2[j]])
            # add next element from nums2 into heap if available
            if j < len(nums2)-1: 
                heappush(heap, [nums1[i]+nums2[j+1], i, j+1])

        return result