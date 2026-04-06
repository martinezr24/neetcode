class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        u_chars = set()
        lp, rp = 0, 0
        longest = 0

        while rp < len(s):
            if s[rp] not in u_chars:
                u_chars.add(s[rp])
                rp += 1
                if len(u_chars) > longest:
                    longest = len(u_chars)
            else:
                u_chars.remove(s[lp])
                lp += 1
        return longest