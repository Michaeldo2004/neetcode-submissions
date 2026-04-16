class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        out = n * [0]
        stack = []
        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((i, temp))
            else:
                while stack and stack[-1][1] < temp:
                    j, curr = stack.pop()
                    out[j] = i - j
                stack.append((i, temp))
        
        return out