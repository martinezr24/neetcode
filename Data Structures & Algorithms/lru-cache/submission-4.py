class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm = dict()
        self.key_arr = []

    def get(self, key: int) -> int:
        if key in self.hm:
            self.key_arr.remove(key)
            self.key_arr.append(key)
            return self.hm[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self.hm[key] = value
            self.key_arr.remove(key)
            self.key_arr.append(key)
            return

        if len(self.hm) == self.capacity:
            lru = self.key_arr.pop(0)
            self.hm.pop(lru)
        
        self.hm[key] = value
        self.key_arr.append(key)

                


