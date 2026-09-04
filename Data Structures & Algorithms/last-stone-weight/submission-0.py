class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        # h = []
        # [2, 2, 3, 4, 6]

        # [2, 2, 3, 2]

        # [2, 2, 2, 3]

        # [1, 2, 2]

        # [1]

        while len(stones) > 1:
            l = stones.pop()
            sl = stones.pop()

            new = l - sl

            if new != 0:
                stones.append(new)
            stones.sort()
        if len(stones) == 1:
            return stones[0]
        else:
            return 0
