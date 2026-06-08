from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        counts = defaultdict(int)
        n = len(s)
        ret = -1

        while r < n:
            counts[s[r]] += 1
            max_c = counts[max(counts, key = counts.get)]

            cur_len = len(s[l:r + 1])

            if cur_len - max_c > k:
                while l <= r and (r-l+1)- max_c > k:
                    counts[s[l]] -= 1
                    l += 1
            else:
                ret = max(ret, cur_len)
            r += 1
        return ret