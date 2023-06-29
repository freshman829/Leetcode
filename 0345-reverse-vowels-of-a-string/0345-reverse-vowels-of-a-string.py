class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        str_vowel = []
        res = ""
        for i in s:
            if i in vowels:
                str_vowel.append(i)
        str_vowel = str_vowel[::-1]
        for i in range(len(s)):
            if s[i] not in vowels:
                res += s[i]
            else:
                res += str_vowel.pop(0)
        return res
             