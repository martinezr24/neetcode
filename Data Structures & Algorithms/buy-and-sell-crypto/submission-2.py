class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0

        l, r = 0, 1

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                max_p = max(max_p, prices[r] - prices[l])
            r += 1
        
        return max_p