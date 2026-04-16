class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        c = [1] * len(nums)

        for i in range(len(nums) -1 , -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    c[i] = max(c[i], 1 + c[j])
        return max(c)
