class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # val : index

        for i in range(len(nums)):
            # check if number in seen can add with i to add up to target
            if (target - nums[i]) in seen.keys():
                return [seen[(target - nums[i])], i]
            else:
                seen[nums[i]] = i
        return []
    