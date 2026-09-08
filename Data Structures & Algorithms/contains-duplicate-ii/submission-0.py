class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                for num in seen[nums[i]]:
                    if abs(i - num) <= k:
                        return True
                seen[nums[i]].append(i)
            else:
                seen[nums[i]] = [i]
        
        return False