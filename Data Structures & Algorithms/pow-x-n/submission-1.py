class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0
        if n == 0: return 1
        if n < 0:
            x = 1/x
            n = abs(n)
        def helper(carry, x, n):
            if n == 1:
                return carry * x
            if n%2 == 0:
                return helper(carry, x**2, n//2)
            else:
                return helper(carry*x, x, n-1)
        

        return helper(1, x, n)