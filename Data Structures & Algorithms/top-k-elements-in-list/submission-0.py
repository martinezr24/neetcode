from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h_map = defaultdict(int)
        ret = []

        for num in nums:
            h_map[num] += 1

        final = [[] for x in range(max(h_map.values()) + 1)]

        for key in h_map:
            print(h_map[key])
            final[h_map[key]].append(key)
        
        ret = []
        for i in range(len(final) - 1, 0, -1):
            if len(ret) == k:
                break
            else:
                for j in final[i]:
                    if len(ret) == k:
                        break
                    ret.append(j)
        return ret




