class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""

        for i in range(len(strs[0])):
            add = True
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or (strs[j][i] != strs[0][i]):
                    return longest

            longest += strs[0][i]
        return longest