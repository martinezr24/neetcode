class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 0:
            return 0
        if n == 1:
            return cost[0]
    
        dp0, dp1 = 0, 0  
        
        for i in range(2, n + 1):
            dp2 = min(dp1 + cost[i - 1], dp0 + cost[i - 2])
            dp0, dp1 = dp1, dp2

        return dp1