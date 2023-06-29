class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                prev = flowerbed[i - 1] if i - 1 >= 0 else 0
                next = flowerbed[i + 1] if i + 1 < length else 0

                if prev == 0 and next == 0:
                    count += 1
                    flowerbed[i] = 1

        return count >= n