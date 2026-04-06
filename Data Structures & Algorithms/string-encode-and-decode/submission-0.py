class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for element in strs:
            element += '||'
            ret += element
        return ret

    def decode(self, s: str) -> List[str]:
        ret = s.split('||')
        return ret[:-1]