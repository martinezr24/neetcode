
class FileSystem:

    def __init__(self):
        self.paths = {'': 0}

        
    def createPath(self, path: str, value: int) -> bool:
        for i in range (len(path) -1, -1, -1):
            if path[i] == '/':
                break
        
        if path in self.paths or path[:i] not in self.paths:
            return False
        else:
            self.paths[path] = value
            return True

    def get(self, path: str) -> int:
        if path in self.paths:
            return self.paths[path]
        else:
            return -1
    



# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
