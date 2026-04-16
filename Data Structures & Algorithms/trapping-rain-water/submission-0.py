class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = n * [0]
        maxRight = n * [0]
        minBoth = n * [0]
        rain = 0

        currMax = 0
        for i in range(1, n):
            if height[i -1] > currMax:
                currMax = height[i-1]
            maxLeft[i] = currMax

        currMax = 0
        for i in range(n-2, -1, -1):
            if height[i + 1] > currMax:
                currMax = height[i + 1]
            maxRight[i] = currMax

        for i in range(1, n):
            minBoth[i] = min(maxLeft[i], maxRight[i])
            currRain = minBoth[i] - height[i]
            if currRain > 0:
                rain += currRain
                
        return rain

        
