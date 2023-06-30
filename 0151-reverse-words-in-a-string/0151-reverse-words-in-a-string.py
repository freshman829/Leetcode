class Solution(object):
    def reverseWords(self, s):
        word_arr = s.split()[::-1]
        return " ".join(word_arr)
        """
        :type s: str
        :rtype: str
        """
        