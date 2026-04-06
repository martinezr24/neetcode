class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []

        def dfs(i, cur_arr, total):
            if total == target:
                ret.append(list(cur_arr))
                return
            if total > target or i >= len(nums):
                return

            temp = cur_arr.copy()
            temp.append(nums[i])
            dfs(i, temp, total + nums[i])
            dfs(i + 1, cur_arr, total)

            return 

        dfs(0, [], 0)
        return ret