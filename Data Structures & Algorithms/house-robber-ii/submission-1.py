class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 3:
            if n == 2:
                return max(nums[1], nums[0])
            else:
                return nums[0]
        
        rob1, rob2 = nums[0], max(nums[1], nums[0])

        for i in range(2, n - 1):
            rob1, rob2 = rob2, max(rob2, rob1 + nums[i])

        op1 = rob2

        rob1, rob2 = nums[1], max(nums[1], nums[2])

        for i in range(3, n):
            rob1, rob2 = rob2, max(rob2, rob1 + nums[i])
        
        return max(op1, rob2)


