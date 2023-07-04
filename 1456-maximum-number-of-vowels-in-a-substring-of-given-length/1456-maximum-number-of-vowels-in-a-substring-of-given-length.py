class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def isVowel(char):
            return char in ['a', 'e', 'i', 'o', 'u']

        max_vowels = 0
        current_vowels = 0

        # Count vowels in first window of size k
        for i in range(k):
            if isVowel(s[i]):
                current_vowels += 1

        max_vowels = current_vowels

        # Slide the window and update vowel counts
        for i in range(k, len(s)):
            if isVowel(s[i - k]):
                current_vowels -= 1

            if isVowel(s[i]):
                current_vowels += 1

            max_vowels = max(max_vowels, current_vowels)

        return max_vowels