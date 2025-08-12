class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        adj_list = [[] for _ in range(n)]
        for i in range(len(prerequisites)):
            v, u = prerequisites[i]
            adj_list[u].append(v)
        
        
        visited = [False for _ in range(n)]
        q = [False for _ in range(n)]
        stack = []

        def hasCycle(u):
            if q[u]:
                return True
            if visited[u]:
                return False
            visited[u] = True
            q[u] = True
            for v in adj_list[u]:
                if hasCycle(v):
                    return True
            q[u] = False
            stack.append(u)
            return False

        for u in range(n):
            if not visited[u] and hasCycle(u):
                return []

        return stack[::-1]
        