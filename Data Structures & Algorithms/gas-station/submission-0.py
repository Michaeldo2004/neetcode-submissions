class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        currGas = 0
        index = 0
        if sum(gas) < sum(cost):
            return -1
        for i in range(len(gas)):
            currGas += gas[i] - cost[i]
            if currGas < 0:
                currGas = 0
                index = i +1
        return index
                