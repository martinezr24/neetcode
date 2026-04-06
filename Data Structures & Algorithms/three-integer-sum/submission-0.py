class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            offset = nums[i]

            while l < r:
                s = nums[r] + nums[l] + nums[i]
                if s == 0:
                    ret.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return ret
                

        