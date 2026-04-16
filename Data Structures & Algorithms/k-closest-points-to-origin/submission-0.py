import heapq
import math
class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = math.sqrt(point[0]**2 + point[1]**2)
            if len(heap) < k:
                heapq.heappush(heap, (-dist, point))
            elif -heap[0][0] > dist:
                heapq.heappop(heap)
                heapq.heappush(heap, (-dist, point))
        
        returner = []
        for i in range(k):
            returner.append(heap[i][1])
        return returner
