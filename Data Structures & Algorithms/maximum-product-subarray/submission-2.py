class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        maxprod = nums[0]
        minprod = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                maxprod, minprod = minprod, maxprod
            
            maxprod = max(maxprod * nums[i], nums[i])
            minprod = min(minprod * nums[i], nums[i])

            res = max(maxprod, res)

        return res