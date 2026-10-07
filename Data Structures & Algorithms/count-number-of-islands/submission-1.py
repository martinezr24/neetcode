from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        row, col = len(grid), len(grid[0])
        count = 0
        seen = set()

        def bfs(r, c):
            q = collections.deque()
            seen.add((r, c))
            q.append((r, c))

            while q:
                cur = q.popleft()
                
                dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

                for dr, dc in dirs:
                    new_r, new_c = cur[0] + dr, cur[1] + dc

                    if new_r >= 0 and new_r < row and new_c >= 0 and new_c < col:
                        if grid[new_r][new_c] == '1' and (new_r, new_c) not in seen:
                            seen.add((new_r, new_c))
                            q.append((new_r, new_c))
            
    
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1' and (r, c) not in seen:
                    bfs(r, c)
                    count += 1
        return count