class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        smallest = 9999

        l, tol = 0, 0

        for r in range(len(nums)):
            tol += nums[r]

            while tol >= target:
                smallest = min(smallest, r - l + 1)
                tol -= nums[l]
                l += 1
            
        return smallest if smallest != 9999 else 0

