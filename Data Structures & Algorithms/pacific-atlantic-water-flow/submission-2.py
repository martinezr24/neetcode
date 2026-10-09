class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac_touch = set()
        atl_touch = set()
        row, col = len(heights), len(heights[0])

        def dfs(start_r, start_c, visited):
            stack = [(start_r, start_c)]
            visited.add((start_r, start_c)) 

            while stack:
                cur_r, cur_c = stack.pop()
                cur_height = heights[cur_r][cur_c]

                dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in dirs:
                    nr, nc = cur_r + dr, cur_c + dc

                    if 0 <= nr < row and 0 <= nc < col and (nr, nc) not in visited:
                        if heights[nr][nc] >= cur_height:
                            visited.add((nr, nc))
                            stack.append((nr, nc))

        for r in range(row):
            dfs(r, 0, pac_touch)           
            dfs(r, col - 1, atl_touch)     

        for c in range(col):
            dfs(0, c, pac_touch)           
            dfs(row - 1, c, atl_touch)     
        
        ret = []
        for val in pac_touch:
            if val in atl_touch:
                ret.append([val[0], val[1]])
                
        return ret