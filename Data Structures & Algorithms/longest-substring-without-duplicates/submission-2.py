class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        maxlen = 0
        while r < len(s):
            while s[r] in s[l:r] and l < r:
                maxlen = max(maxlen, r - l)
                l += 1
            r +=1
        return max(maxlen, r-l)
