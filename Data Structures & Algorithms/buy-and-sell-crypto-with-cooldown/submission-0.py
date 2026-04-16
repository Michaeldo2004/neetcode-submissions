class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}

        def dfs(i, buy):
            if i >= len(prices):
                return 0 

            if (i, buy) in memo:
                return memo[(i, buy)]
            
            if buy:
                memo[(i, buy)] = max(-prices[i] + dfs(i+1, buy=False), dfs(i+1, buy=True))
            else:
                memo[(i, buy)] = max(prices[i] + dfs(i+2, buy=True), dfs(i+1, buy))
            
            return memo[(i, buy)]
        return dfs(0, True)