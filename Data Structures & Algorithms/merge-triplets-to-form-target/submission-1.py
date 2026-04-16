class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if len(triplets) == 1:
            return target == triplets[0]
        exists = set()
        for i in range(len(triplets)):
            if triplets[i][0] <= target[0] and triplets[i][1] <= target[1] and triplets[i][2] <= target[2]:
                if triplets[i][0] == target[0]:
                    exists.add(0)
                if triplets[i][1] == target[1]:
                    exists.add(1)
                if triplets[i][2] == target[2]:
                    exists.add(2)
            if len(exists) == 3:
                return True

        

            
        return False
        