class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_map = {}
        for num in arr:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1

        count_set = set()
        for count in count_map.values():
            if count in count_set:
                return False
            count_set.add(count)

        return True