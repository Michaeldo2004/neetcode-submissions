class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
            if not self.minHeap or self.minHeap[0] < num:
                heapq.heappush(self.minHeap, num)
            else:
                heapq.heappush(self.maxHeap, -num)
            
            if abs(len(self.minHeap) - len(self.maxHeap)) > 1:
                if len(self.minHeap) > len(self.maxHeap):
                    someNum = heapq.heappop(self.minHeap)
                    heapq.heappush(self.maxHeap, -someNum)
                else:
                    someNum = heapq.heappop(self.maxHeap)
                    heapq.heappush(self.minHeap, -someNum)
        

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return float((-self.maxHeap[0] + self.minHeap[0]) /2)
        else: 
            return self.minHeap[0] if len(self.minHeap) > len(self.maxHeap) else -self.maxHeap[0]
        
        