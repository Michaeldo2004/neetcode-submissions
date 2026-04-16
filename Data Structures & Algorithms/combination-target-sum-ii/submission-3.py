class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        r = []

        def dfs(i,l, s):
            if s == target:
                r.append(l.copy())
                return
            if s > target or i == len(candidates):
                return

            
            l.append(candidates[i])
            dfs(i + 1, l, s + candidates[i])
            l.pop()

            while i+1< len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, l, s)
        dfs(0, [], 0)
        return r
