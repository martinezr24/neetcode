import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        ret = r
        while l <= r:
            k = (l + r) // 2

            hours = 0
            for num in piles:
                hours += math.ceil(num / k)
            if hours > h:
                l = k + 1
            else:
                r = k - 1
                ret = k
        return ret


            