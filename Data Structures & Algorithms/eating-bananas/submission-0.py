class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles) 
        spd = r
        while l <= r:
            m = (l + r)//2
            currHr = 0
            for pile in piles:
                currHr += math.ceil(pile/m)
            if currHr <= h:
                spd = m
                r = m -1
            else:
                l = m +1
        return spd