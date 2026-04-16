class Solution:

    def getSquareSum(self, n: int) -> int:
        t = 0
        for c in str(n):
            t += int(c) ** 2
        return t
    
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)
            n = self.getSquareSum(n)
            if n == 1: return True
        return False