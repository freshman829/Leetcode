class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        ret = []
        zero = []
        for key, val in enumerate(nums):
            if val == 0:
                zero.append(key)
            else:
                total *= val
        for key, val in enumerate(nums):
            if val != 0 and len(zero) == 0:
                ret.append(total // val)
            elif val != 0 and len(zero) > 0 or val == 0 and len(zero) > 1:
                ret.append(0)
            elif val == 0 and len(zero) == 1:
                ret.append(total)
        return ret