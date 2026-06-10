class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = dict()
        ret = []

        for i in range(len(strs)):
            arr = [0] * 26
            for j in range(len(strs[i])):
                arr[ord(strs[i][j]) - ord('a')] += 1
            key = tuple(arr)
            if key not in dct:
                dct[key] = [strs[i]]
            else:
                dct[key].append(strs[i])
        
        for ele in dct:
            ret.append(dct[ele])
        return ret


