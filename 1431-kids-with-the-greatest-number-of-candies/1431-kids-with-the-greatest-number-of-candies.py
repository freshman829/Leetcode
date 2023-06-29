class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        new_list = list(candies)
        new_list.sort()
        largest_candies = new_list[-1]
        res = []
        for i in candies:
            if i + extraCandies >= largest_candies:
                res.append(True)
            else:
                res.append(False)
        return res