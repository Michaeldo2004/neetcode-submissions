class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         numList = sorted(nums)
         for i in range (1, len(numList)):
            if numList[i-1] == numList[i]:
                return True
         return False