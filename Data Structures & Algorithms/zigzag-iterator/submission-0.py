class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.v1p = 0
        self.v2p = 0

        self.which = 1

    def next(self) -> int:
        if self.which == 1:
            if self.v1p >= len(self.v1):
                self.which = 2
        
        if self.which == 2:
            if self.v2p >= len(self.v2):
                self.which = 1
        
        if self.which == 1:
            self.which = 2
            self.v1p += 1
            return self.v1[self.v1p - 1]
        else:
            self.which = 1
            self.v2p += 1
            return self.v2[self.v2p - 1]

    def hasNext(self) -> bool:
        if self.v1p < len(self.v1) or self.v2p < len(self.v2):
            return True
        return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
