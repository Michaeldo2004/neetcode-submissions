class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pref = [0] * len(nums)
        post = [0] * len(nums)
        out = [0] * len(nums)

        pref[0] = nums[0]
        for i in range(1, len(nums)):
            pref[i] = nums[i] * pref[i-1]
        post[-1] = nums[-1]
        for j in range(len(nums) -2, -1, -1):
            post[j] = nums[j] * post[j+1]

        out[0] = post[1]
        out[-1] = pref[-2]
        for k in range(1, len(nums)-1):
            out[k] = pref[k-1] * post[k+1]
            
        return out
        