class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # loop through and first find indices of rotten fruits
        # for each index we do bfs starting at that index and seen how many counts it takes for all fruits to be rotten next to it
        # loop again through the grid and see if any are unrotten. if they are return -1, else return max of each bfs

        q = deque()
        fresh_count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1
                    
        time_passed = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while q and fresh_count > 0:
            n = len(q)
            for _ in range(n):
                ci, cj = q.popleft()
                
                for di, dj in directions:
                    ni, nj = ci + di, cj + dj
                    
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 1:
                        grid[ni][nj] = 2  
                        q.append((ni, nj))
                        fresh_count -= 1
                        
            time_passed += 1
            
        return time_passed if fresh_count == 0 else -1


