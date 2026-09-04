import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
     
        # h = []
        # [2, 2, 3, 4, 6]

        # [2, 2, 3, 2]

        # [2, 2, 2, 3]

        # [1, 2, 2]

        # [1]
        heapq.heapify_max(stones)

        while len(stones) > 1:
            e1 = heapq.heappop_max(stones)
            e2 = heapq.heappop_max(stones)

            fin = e1 - e2

            if fin != 0:
                heapq.heappush_max(stones, fin)
        
        if len(stones) == 1:
            return stones[0]
        else:
            return 0
