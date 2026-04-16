class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums)%2:
            return False
        
        target = sum(nums)//2
        memo = {}

        def dfs(i, target):
            if target == 0:
                return True
            if i >= len(nums):
                return False
            if (i, target) in memo.keys():
                return memo[(i, target)]
            
            if dfs(i+1, target-nums[i]) or dfs(i+1, target):
                memo[(i, target)] = True
                return True
            
            memo[(i, target)] = False
            return False
        print(memo)
        return dfs(0, target)
            
