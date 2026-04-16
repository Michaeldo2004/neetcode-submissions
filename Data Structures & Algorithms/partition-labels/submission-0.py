class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i in range(len(s)):
            lastIndex[s[i]] = i
        returned = []
        size = 0
        end = 0
        for i in range(len(s)):
            size +=1
            end = max(end, lastIndex[s[i]])
            if i == end:
                returned.append(size)
                size = 0
        return returned


            
        