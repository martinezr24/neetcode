class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = 0
        actual = 0

        for i in range(n + 1):
            expected += i
        
        for j in range(n):
            actual += nums[j]
        
        return expected - actual