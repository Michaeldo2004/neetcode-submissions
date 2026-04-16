class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
            #hash map of frequency
        count = Counter(hand)
        hand.sort()
        
        for num in hand:
            if count[num]:  #if num exists
                for i in range(num, num + groupSize):
                    if not count[i]:
                        return False
                    else:
                        count[i] -=1
        return True

