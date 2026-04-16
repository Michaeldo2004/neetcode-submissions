class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        r = []
        def dfs(i, l, t):
            if t == target:
                r.append(l.copy())
                return
            if i >= len(nums) or t > target:
                return
            l.append(nums[i])
            dfs(i, l, t + nums[i])
            l.pop()
            dfs(i + 1, l, t)
        dfs(0, [], 0)
        return r