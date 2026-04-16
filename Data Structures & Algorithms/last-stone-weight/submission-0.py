import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            stoneA = heapq.heappop_max(stones)
            stoneB = heapq.heappop_max(stones)
            if stoneA - stoneB > 0:
                heapq.heappush_max(stones, stoneA-stoneB)
        return stones[0] if stones else 0