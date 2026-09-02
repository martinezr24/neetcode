class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # loop through each number in the grid
        # if it's a 1, do dfs starting at that number
        # change that 1 and every adjacent 1 to a 3
        # increment count by 1
        # return count

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(i, j, grid)
                    count += 1
            
        return count
        

    def dfs(self, i, j, grid):
        if i >= len(grid) or i < 0:
            return
        if j >= len(grid[0]) or j < 0:
            return
        if grid[i][j] != '1':
            return

        grid[i][j] = '3'
        self.dfs(i + 1, j, grid)
        self.dfs(i - 1, j, grid)
        self.dfs(i, j + 1, grid)
        self.dfs(i, j - 1, grid)