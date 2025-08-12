class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        adj_list = [[] for _ in range(n)]
        for i in range(len(prerequisites)):
            v, u = prerequisites[i]
            adj_list[u].append(v)

        visited = [False for _ in range(n)]
        q = [False for _ in range(n)]

        def hasCycle(u, visited, q):
            if q[u]:
                return True
            if visited[u]:
                return False
            visited[u] = True
            q[u] = True
            for v in adj_list[u]:
                if hasCycle(v, visited, q):
                    return True
            q[u] = False
            return False

        for u in range(n):
            # q = set()
            if not visited[u] and hasCycle(u, visited, q):
                return False
        return True
