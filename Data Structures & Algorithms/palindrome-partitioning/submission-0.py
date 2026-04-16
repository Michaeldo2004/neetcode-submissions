class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        r = []

        def dfs(i, l):
            if i == n:
                r.append(l.copy())
                return
            for j in range(i, n):
                substring = s[i:j+1]
                if substring == substring[::-1]:
                    l.append(substring)
                    dfs(j+1, l)
                    l.pop()
        dfs(0,[])
        return r