class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        ast = []
        for i, c in enumerate(s):
            if c == '(':
                left.append(i)
            elif c == '*':
                ast.append(i)
            else:
                if not left and not ast:
                    return False
                if left:
                    left.pop()
                else:
                    ast.pop()
        while left and ast:
            if left.pop() > ast.pop():
                return False
        return not left
        
            
        