class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.grid = [[0] * n for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        if self.grid[row][col] != 0:
            raise ValueError("spot already taken")
        
        self.grid[row][col] = player

        dirs = [(0, 1), (1, 0), (1, 1), (-1, 1)]

        highest = 0
        for dr, dc in dirs:
            count = 1

            nr, nc = row + dr, col + dc
            while 0 <= nr < self.n and 0 <= nc < self.n and self.grid[nr][nc] == player:
                count += 1
                nr += dr
                nc += dc
                
            nr, nc = row - dr, col - dc
            while 0 <= nr < self.n and 0 <= nc < self.n and self.grid[nr][nc] == player:
                count += 1
                nr -= dr
                nc -= dc

            highest = max(highest, count)

        
        if highest >= self.n:
            return player
        else: 
            return 0



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
