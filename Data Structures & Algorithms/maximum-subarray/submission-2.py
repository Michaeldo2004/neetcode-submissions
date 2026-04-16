class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = None
        sumMax = -1001
        for num in nums:
            # base case
            if currSum is None or currSum < 0:
                currSum = num
                if currSum is not None:
                    sumMax = max(sumMax, currSum)
            # resets sum
            elif currSum + num <= 0:
                sumMax = max(sumMax, currSum)
                currSum = None
            else:
                currSum += num
                sumMax = max(sumMax, currSum)
        return max(sumMax, currSum)