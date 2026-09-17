class TrieNode:
    def __init__(self):
        self.children = {}
        self.content = ""
        self.is_file = False

class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> List[str]:
        cur = self.root
        components = [p for p in path.split('/') if p]

        for c in components:
            cur = cur.children[c]
        
        if cur.is_file:
            return [components[-1]]
        else:
            return sorted(cur.children)

    def mkdir(self, path: str) -> None:
        cur = self.root
        components = [p for p in path.split('/') if p]

        for c in components:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

    def addContentToFile(self, filePath: str, content: str) -> None:
        cur = self.root
        components = [p for p in filePath.split('/') if p]

        for c in components:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.is_file = True
        cur.content += content

    def readContentFromFile(self, filePath: str) -> str:
        cur = self.root
        components = [p for p in filePath.split('/') if p]

        for c in components:
            cur = cur.children[c]

        return cur.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
