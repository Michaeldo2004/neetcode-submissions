class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) -1, -1, -1):
            if carry > 0:
                digits[i] += carry
                carry -=1
            
            if digits[i] > 9:
                digits[i] %= 10
                carry += 1
        return [carry] + digits if carry else digits
            