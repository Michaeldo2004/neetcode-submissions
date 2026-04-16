class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = []
        r = []

        for i in range(len(nums)):
            heapq.heappush(q, (-nums[i], i))
            if i >= k-1:
                while q[0][1] <= i - k:
                    heapq.heappop(q)
                r.append(-q[0][0])
        return r

        