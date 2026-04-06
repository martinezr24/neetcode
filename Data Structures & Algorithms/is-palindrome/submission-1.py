class Solution:
    def isPalindrome(self, s: str) -> bool:
        ind_f = 0
        ind_b = len(s) - 1

        while ind_f < len(s):
            if s[ind_f].isalnum() and s[ind_b].isalnum():
                if s[ind_f].lower() == s[ind_b].lower():
                    ind_f += 1
                    ind_b -= 1
                else:
                    return False
            else:
                if not s[ind_f].isalnum():
                    ind_f += 1
                else:
                    ind_b -= 1
        return True



        