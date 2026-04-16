class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        r = []

        def dfs(l):
            if len(l) == len(nums):
                r.append(l.copy())
                return
            if len(l) >= len(nums):
                return
            for num in nums:
                if num not in l:
                    l.append(num)
                    dfs(l)
                    l.pop()            
        dfs([])
        return r

            

        