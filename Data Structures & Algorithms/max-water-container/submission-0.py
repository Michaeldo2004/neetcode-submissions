class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) -1
        area = 0

        while i < j:
            length = min(heights[i], heights[j])
            area = max(length * abs(j - i), area)
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return area