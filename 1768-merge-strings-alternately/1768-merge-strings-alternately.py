class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        str = ""
        short_len = min(len(word1), len(word2))
        for i in range(short_len):
            str += word1[i]
            str += word2[i]
        if len(word1) == len(word2):
            return str
        elif len(word1) < len(word2):
            sli = slice (short_len, len(word2))
            str += word2[sli]
        else:
            sli = slice (short_len, len(word1))
            str += word1[sli]
        return str