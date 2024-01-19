class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
    
        for i in range(1, n):
            for j in range(n):
                matrix[i][j] += min(matrix[i-1][max(0, j-1):min(n, j+2)])

        return min(matrix[-1])
        # minSum = 0
        # minIndex = 0
        # for idx, row in enumerate(matrix):
        #     if idx == 0:
        #         minSum += min(row)
        #         minIndex = row.index(min(row))
        #     else:
        #         if minIndex <= 0:
        #             minSum += min(row[minIndex], row[minIndex + 1])
        #             minIndex = minIndex if row[minIndex] < row[minIndex + 1] else minIndex + 1
        #         elif minIndex >= len(row) - 1:
        #             print(idx, minIndex, "go")
        #             minSum += min(row[minIndex], row[minIndex - 1])
        #             if row[minIndex] > row[minIndex - 1]:
        #                 minIndex = minIndex - 1    
        #                 print(idx, minIndex)
        #             print(idx, minIndex, "hiho")
        #         else:
        #             minSum += min(row[minIndex], row[minIndex - 1], row[minIndex + 1])
        #             if row[minIndex] > row[minIndex + 1] and row[minIndex + 1] < row[minIndex - 1]:
        #                 minIndex = minIndex + 1
        #             elif row[minIndex] > row[minIndex - 1] and row[minIndex + 1] > row[minIndex - 1]:
        #                 minIndex = minIndex - 1
        #             print(idx, minIndex, "hiho")
        #     print(minSum)
        # return minSum