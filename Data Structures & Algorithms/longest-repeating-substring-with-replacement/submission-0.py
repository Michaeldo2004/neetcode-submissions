class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charDict = {}
        sublen = 0
        l = 0
        r = 0

        while r < len(s):
            if s[r] in charDict.keys():
                charDict[s[r]] += 1 
            else:
                charDict[s[r]] = 1
            while l < r and r - l + 1 - max(charDict.values()) > k:
                charDict[s[l]] -=1
                l += 1
            
            r += 1
            sublen = max(r-l, sublen)
        
        return sublen

        