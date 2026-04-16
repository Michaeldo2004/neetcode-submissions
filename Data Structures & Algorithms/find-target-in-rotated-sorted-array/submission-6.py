class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:

            m = (l + r) // 2
            if nums[m] == target: return m

            if nums[l] <= nums[m]: # checking left side
                if nums[m] < target or target < nums[l]: # if smallest is bigger -> cannot be on the left side
                    l = m + 1
                else:
                    r = m - 1
            else: # check right side
                if nums[m] > target or target > nums[r]: # if target is bigger than the biggest -> cannot be on
                    r = m - 1                            # the right side
                else:
                    l = m + 1
            
        return -1
        