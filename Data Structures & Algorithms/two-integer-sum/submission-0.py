class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = []
        for i in range(len(nums)):
            if target - nums[i] in numbers:
                return [numbers.index(target - nums[i]), i]
            else:
                numbers.append(nums[i])

        