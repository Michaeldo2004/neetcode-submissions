class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1C, s2C = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1C[ord(s1[i]) - ord('a')] += 1
            s2C[ord(s2[i]) - ord('a')] += 1
        
        match = 0
        for i in range(26):
            match += (1 if s1C[i] == s2C[i] else 0)
        l = 0
        for r in range(len(s1), len(s2)):
            if match == 26: return True
            
            currIndex = ord(s2[r]) - ord('a')
            s2C[currIndex] += 1
            if s1C[currIndex] == s2C[currIndex]:
                match +=1
            elif s1C[currIndex] +1 == s2C[currIndex]:
                match -=1

            currIndex = ord(s2[l]) - ord('a')
            s2C[currIndex] -= 1
            if s1C[currIndex] == s2C[currIndex]:
                match +=1
            elif s1C[currIndex] -1 == s2C[currIndex]:
                match -=1
            l += 1
        return match == 26

        