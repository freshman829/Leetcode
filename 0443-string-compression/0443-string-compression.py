class Solution:
    def compress(self, chars: List[str]) -> int:
        writeIndex = 0
        count = 1
        n = len(chars)

        for i in range(1, n):
            if chars[i] == chars[i-1]:
                count += 1
            else:
                chars[writeIndex] = chars[i-1]
                writeIndex += 1

                if count > 1:
                    count_str = str(count)
                    for digit in count_str:
                        chars[writeIndex] = digit
                        writeIndex += 1

                count = 1

        chars[writeIndex] = chars[n-1]
        writeIndex += 1

        if count > 1:
            count_str = str(count)
            for digit in count_str:
                chars[writeIndex] = digit
                writeIndex += 1

        return writeIndex