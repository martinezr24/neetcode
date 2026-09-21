from collections import deque

class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.q = deque()

        if v1:
            self.q.append((v1, 0))
        if v2:
            self.q.append((v2, 0))

    def next(self) -> int:
        cur, ind = self.q.popleft()
        
        if ind + 1 < len(cur):
            self.q.append((cur, ind + 1))
        
        return cur[ind]

    def hasNext(self) -> bool:
        return len(self.q) > 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
