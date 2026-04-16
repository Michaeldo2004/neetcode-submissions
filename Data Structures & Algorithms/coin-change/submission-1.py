class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        c = [amount + 1] * (amount +1)
        c[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    c[a] = min(c[a], 1 + c[a-coin])
        return c[amount] if c[amount] <= amount else -1