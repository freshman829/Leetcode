class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_count = 0
        max_length = 0
        start = 0
        freq = {'T': 0, 'F': 0}

        for end in range(len(answerKey)):
            freq[answerKey[end]] += 1
            max_count = max(max_count, freq[answerKey[end]])

            if (end - start + 1) - max_count > k:
                freq[answerKey[start]] -= 1
                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length
