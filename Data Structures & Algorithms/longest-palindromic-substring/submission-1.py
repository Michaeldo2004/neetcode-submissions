class Solution:
    def longestPalindrome(self, s: str) -> str:
        l_idx = 0
        len_r = 0

        for i in range(len(s)):
            # odd length
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l > len_r:
                    len_r = r - l
                    l_idx = l
                l -=1
                r +=1
            # even length
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l > len_r:
                    len_r = r - l
                    l_idx = l
                l -=1
                r +=1
        return s[l_idx: l_idx + len_r + 1]