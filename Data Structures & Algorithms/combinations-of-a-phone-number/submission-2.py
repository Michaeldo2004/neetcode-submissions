class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_lookup = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv", 
            9: "wxyz"
        }
        r = []
        def dfs(string, i):
            if len(string) == len(digits):
                r.append(string)
                return
            if i > len(digits):
                return
            
            for char in num_lookup[int(digits[i])]:
                dfs(string+char, i+1)
            
        dfs("", 0)
        return r if r and digits else []