class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = {}
        freq2 = {}
        for i in s:
            if not i in freq1:
                freq1[i] = 1
            else :
                freq1[i] +=1
        for i in t:
            if not i in freq2:
                freq2[i] = 1
            else :
                freq2[i] +=1
        return freq1 == freq2
        

        