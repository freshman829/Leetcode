class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        length = 0
        arr = []
        
        if n > m:
            length = n
        else:
            length = m
        for i in range(length):
            if i < m:
                arr.append(nums1[i])
            if i < n:
                arr.append(nums2[i])
        arr.sort()
        if len(arr) % 2 != 0:
            return arr[int((len(arr) - 1) / 2)]
        else:
            return (arr[int(len(arr) / 2)] + arr[int(len(arr) / 2) - 1]) / 2