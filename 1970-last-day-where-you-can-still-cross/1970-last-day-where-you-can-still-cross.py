class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def isPossible(day):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            matrix = [[0] * col for _ in range(row)]
            for i in range(day):
                r, c = cells[i]
                matrix[r - 1][c - 1] = 1

            visited = set()

            def dfs(r, c):
                if r == row:
                    return True

                visited.add((r, c))

                for dx, dy in directions:
                    nr, nc = r + dx, c + dy
                    if (
                        1 <= nr <= row
                        and 1 <= nc <= col
                        and (nr, nc) not in visited
                        and matrix[nr - 1][nc - 1] == 0
                    ):
                        if dfs(nr, nc):
                            return True

                return False

            for c in range(1, col + 1):
                if matrix[0][c - 1] == 0 and dfs(1, c):
                    return True

            return False

        left = 0
        right = len(cells)
        result = -1

        while left <= right:
            mid = left + (right - left) // 2
            if isPossible(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result