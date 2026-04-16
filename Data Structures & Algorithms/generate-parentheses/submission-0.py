class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        r = []

        def dfs(string, openC, closeC):
            if openC == n and closeC == n:
                r.append(string)
                return
            
            if openC < n:
                dfs(string+ "(", openC+1, closeC)
            if closeC < openC:
                dfs(string+ ")", openC, closeC+1)

        dfs("", 0, 0)
        return r