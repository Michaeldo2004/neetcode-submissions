class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = {}
        v = [0] * numCourses
        for prereq in prerequisites:
            if prereq[0] not in pre:
                pre[prereq[0]] = []
            pre[prereq[0]].append(prereq[1])

        def dfs(i):
            if v[i] == 1: return False
            if v[i] == 2: return True

            v[i] = 1
            if i in pre:
                for n in pre[i]:
                    if not dfs(n):
                        return False
            v[i] = 2
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
        