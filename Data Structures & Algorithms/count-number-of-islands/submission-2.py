from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row, col = len(grid), len(grid[0])
        count = 0
        seen = set()

        def bfs(r, c):
            q = deque()
            q.append((r, c))

            while q:
                cur = q.popleft()
                cur_r, cur_c = cur[0], cur[1]

                dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]

                for dr, dc in dirs:
                    nr, nc = cur_r + dr, cur_c + dc

                    if nr >= 0 and nc >= 0 and nr < row and nc < col:
                        if grid[nr][nc] == "1" and (nr, nc) not in seen:
                            seen.add((nr, nc))
                            q.append((nr, nc))


        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1' and (r, c) not in seen:
                    seen.add((r, c))
                    bfs(r, c)
                    count += 1
        return count