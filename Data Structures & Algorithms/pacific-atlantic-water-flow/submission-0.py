class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ret = []
        row, col = len(heights), len(heights[0])


        def dfs(r, c):
            seen = set()
            stack = [(r, c)]
            touch_pac = False
            touch_atl = False

            while stack:
                cur = stack.pop()
                
                dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in dirs:
                    nr, nc = dr + cur[0], dc + cur[1]

                    if nr < 0 or nc < 0:
                        touch_pac = True

                    if nr >= row or nc >= col:
                        touch_atl = True

                    if nr >= 0 and nr < row and nc >= 0 and nc < col:
                        if (nr, nc) not in seen and heights[nr][nc] <= heights[cur[0]][cur[1]]:
                            seen.add((nr, nc))
                            stack.append((nr, nc))

            return True if (touch_pac and touch_atl) else False

        for r in range(row):
            for c in range(col):
                if dfs(r, c):
                    ret.append([r, c])
        return ret