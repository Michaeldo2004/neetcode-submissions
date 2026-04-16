class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memo = {}
        if not nums: return 1
        nums = [1] + nums + [1]

        def dfs(l, r):
            if l >= r:
                return 0

            if (l, r) in memo:
                return memo[(l,r)]
            best = 0
            for k in range(l+1, r):
                best = max(best, nums[k]*nums[l]*nums[r] + dfs(l, k) + dfs(k, r))
            memo[(l,r)] = best
            return memo[(l,r)]
        return dfs(0, len(nums)-1)

