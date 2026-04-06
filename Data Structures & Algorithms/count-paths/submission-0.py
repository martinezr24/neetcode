class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        grid = [[0] * (n + 1) for _ in range (m + 1)]
        grid[-2][-2] = 1

        print(grid)

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                # print(r, c)
                grid[r][c] += (grid[r][c + 1] + grid[r + 1][c])
            print(grid)
        return grid[0][0]



