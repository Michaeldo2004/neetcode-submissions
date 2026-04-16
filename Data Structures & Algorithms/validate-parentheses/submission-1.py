class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matchDict = {"(":")", "{": "}", "[": "]"}
        for c in s:
            if c in matchDict.keys():
                stack.append(c)
            else:
                if not stack or matchDict[stack.pop()] != c:
                    return False
        return not stack
        