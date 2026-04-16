class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        for i in range(len(nums)):
            curr = nums[i]
            for j in range(i + 1, len(nums)):
                curr *= nums[j]
                res = max(res, curr)
        return res