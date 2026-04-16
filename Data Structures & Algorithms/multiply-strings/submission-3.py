class Solution:
    def strsum(self, n1, n2):
        return str(int(n1) + int(n2))

    def multiply(self, num1: str, num2: str) -> str:
        r = "0"

        if len(num1) < len(num2):
            num1, num2 = num2, num1

        for i,dig in enumerate(num2[::-1]):
            curr = ""
            carry = 0
            for num in num1[::-1]:
                n = int(num) * int(dig) + carry
                if n > 9:
                    carry = n//10
                    n %=10
                else:
                    carry = 0
                curr = str(n) + curr
            if carry:
                curr = str(carry) + curr
            
            curr += "0"*i
            print(curr)
            r = self.strsum(curr, r)
        return r