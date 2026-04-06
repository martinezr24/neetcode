class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)

        grid = [[0] * (l1 + 1) for _ in range(l2 + 1)]

        for r in range(l2 - 1, -1, -1):
            for c in range(l1 - 1, -1, -1):
                if text2[r] == text1[c]:
                    grid[r][c] = 1 + grid[r + 1][c + 1]
                else:
                    grid[r][c] = max(grid[r + 1][c], grid[r][c + 1])
        print(grid)
        return grid[0][0]

    #     return self.longest(text1, text2)

    # def longest(self, text1, text2):

    #     while 0 < len(text1) and 0 < len(text2):
    #         if text1[0] == text2[0]:
    #             return 1 + self.longest(text1[1:], text2[1:])
    #         else:
    #             return 0 + max(self.longest(text1[1:], text2[:]), self.longest(text1[:], text2[1:]))
    #     return 0


    