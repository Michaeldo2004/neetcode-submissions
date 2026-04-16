class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortNum = sorted(nums)   # nlogn + n
        rList = []
        for i in range(len(nums)):
            if sortNum[0] > 0:
                break
            if i > 0 and sortNum[i] == sortNum[i-1]:
                continue
            j = i +1
            k = len(nums) -1
            while j < k:
                somesum = sortNum[i] + sortNum[j] + sortNum[k]
                if somesum == 0:
                    rList.append([sortNum[i], sortNum[j], sortNum[k]])
                    k -=1
                    j +=1
                    while j < k and sortNum[k] == sortNum[k+1]:
                        k -=1
                    while j < k and sortNum[j] == sortNum[j-1]:
                        j +=1    
                elif somesum > 0:
                    k -=1
                else:
                    j +=1
        return list(rList)

        