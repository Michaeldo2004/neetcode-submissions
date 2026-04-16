from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = [cnt for cnt in freq.values()]
        heapq.heapify_max(heap)
        q = deque()
        t = 0
        while heap or q:
            t += 1
            if not heap:
                t = q[0][1]
            else:
                c = heapq.heappop_max(heap)
                c -= 1
                if c > 0:
                    q.append((c, t+n))
            while q and q[0][1] == t:
                fr, cd = q.popleft()
                heapq.heappush_max(heap, fr)
        return t
