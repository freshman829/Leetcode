class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i = j = 0
        longest = 0
        str = set()
        
        while i < n and j < n:
            if s[j] not in str:
                str.add(s[j])
                j += 1
                longest = max(longest, j - i)
            else:
                str.remove(s[i])
                i += 1
        return longest