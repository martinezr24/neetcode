class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        highest_count = 0
        h_set = set(nums)

        for num in h_set:
            if num - 1 not in h_set:
                cur = num
                count = 1

                while cur + 1 in h_set:
                    count += 1
                    cur += 1
                highest_count = max(count, highest_count)
        return highest_count
