class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix, postfix, ret = [], [], []

        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                prefix.append(prefix[i - 1] * nums[i - 1])
        print(prefix)

        for i in range(len(nums) -1, -1, -1):
            if i == len(nums) - 1:
                postfix.insert(0, 1)
            else:
                print(i)
                postfix.insert(0, postfix[0] * nums[i + 1])

        for i in range(len(nums)):
            ret.append(prefix[i] * postfix[i])
        return ret

        