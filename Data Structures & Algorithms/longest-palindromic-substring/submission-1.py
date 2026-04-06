class Solution:
    def longestPalindrome(self, s: str) -> str:
        cur_start = None
        cur_end = None
        
        for i in range(len(s)):
            print(str(i) + " "+ str(cur_start) + str(cur_end))
            j = i
            while j < len(s):
                print(s[j] + "=" + str(j) + str(self.isPalindrome(s, i, j)))
                if self.isPalindrome(s, i, j):
                    if (cur_end == None):
                        cur_start = i
                        cur_end = j
                    elif (j - i > cur_end - cur_start):
                        cur_start = i
                        cur_end = j
                j += 1

        if cur_end != None:
            return s[cur_start:cur_end + 1]
        return ""
        
    # def test(self):
    #     print(self.isPalindrome("racecar", 0, 6))

    def isPalindrome(self, s: str, start: int, end: int) -> bool:
        while (not start > end):
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True