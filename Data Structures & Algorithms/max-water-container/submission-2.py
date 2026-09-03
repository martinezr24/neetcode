class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_a = -1

        l, r = 0, len(heights) - 1
        while l < r:
            d = r - l
            cur_a = min(heights[l], heights[r]) * d
            max_a = max(max_a, cur_a)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_a    