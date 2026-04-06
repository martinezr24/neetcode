class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        n_len = len(nums)

        def dfs(cur, options):
            if len(cur) == n_len:
                ret.append(cur.copy())
                return
            
            if len(options) == 0:
                return


            for i in range(len(options)):
                t = options[i]
                cur.append(t)
                options.remove(t)
                dfs(cur, options)
                cur.pop()
                options.insert(i, t)
            
            return
        dfs([], nums)
        return ret