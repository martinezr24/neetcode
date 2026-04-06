class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h_map = {}

        for string in strs:
            s_string = sorted(string)
            s_string = "".join(s_string)
            if s_string in h_map:
                h_map[s_string].append(string)
            else:
                h_map[s_string] = [string]

        return list(h_map.values())
