class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []

        def dfs(cur, o, c):
            if c == o and c == n and o == n:
                ret.append(cur[:])
            
            if o > n or c > n or c > o:
                return
            
            temp = cur[:]
            dfs(temp + '(', o + 1, c)
            dfs(cur + ')', o, c + 1)
            return
        dfs("", 0, 0)
        return ret