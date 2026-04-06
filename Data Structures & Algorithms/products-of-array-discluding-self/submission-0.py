class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ind = 0
        ret = [None for x in range(len(nums))]

        while ind < len(nums):
            for i in range(len(nums)):
                if ind != i:
                    if ret[ind] == None:
                        ret[ind] = nums[i]
                    else:
                        ret[ind] *= nums[i]
            ind += 1
        return ret
        