class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frq = {}

        for num in nums:
            if num in frq:
                frq[num] += 1
            else:
                frq[num] = 1
        
        ret = []
        for i in range(k):
            max_val = max(frq, key=frq.get)
            ret.append(max_val)
            del frq[max_val]
        return ret