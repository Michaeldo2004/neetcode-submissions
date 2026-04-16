class Solution:
    def rob(self, nums: List[int]) -> int:
        c = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0
            if c[i] != -1: return c[i]

            c[i] = nums[i] + max(dfs(i+2), dfs(i + 3))

            return c[i]
        return max(dfs(0), dfs(1))