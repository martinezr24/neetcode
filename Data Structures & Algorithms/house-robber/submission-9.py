class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n

        def dfs(i):

            if i >= n:
                return 0
            
            if dp[i] != -1:
                return dp[i]

            dp[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return dp[i]

        return dfs(0)

        # nums = [2,9,8,3,6]
        # [0, 0, 0, 0, 0]
        # n = 5

        # dfs(0) = max(nums[0] + dfs(2), dfs(1))
        #             2 + dfs(2), dfs(1)
        #                         max(9 + dfs(3), dfs(2))

