class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        maxlen = 0
        someset = set()
        while r < len(s):
            while s[r] in someset and l < r:
                maxlen = max(maxlen, r - l)
                someset.remove(s[l])
                l += 1
            someset.add(s[r])
            r +=1
        return max(maxlen, r-l)
