class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n - 1
        
        max_area = -1
        while l < r:
            cur = (r - l) * min(heights[l], heights[r])
            max_area = max(max_area, cur)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_area
        