class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s) -1
        while p1 < p2:
            if not s[p1].isalnum():
                p1 += 1
                continue
            if not s[p2].isalnum():
                p2 -=1
                continue
            first = s[p1].lower() if not s[p1].isdigit() else s[p1]
            sec = s[p2].lower() if not s[p2].isdigit() else s[p2]
            if first != sec:
                return False
            p1 += 1
            p2 -= 1
        return True