import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sort values by frequency
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        heap = []
        # for each element add to heap of k size and 
        # remove the smallest as the loop continues while heap size = k
        for num, frequency in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (frequency, num))
            elif heap[0][0] < frequency:
                heapq.heappop(heap)
                heapq.heappush(heap, (frequency, num))

        return [num for frequency, num in heap]


        