class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list = {}
        n = len(equations)
        for i in range(n):
            u,v = equations[i]
            x = values[i]

            if u not in adj_list:
                adj_list[u] = {}
            if v not in adj_list:
                adj_list[v] = {}

            adj_list[u][v] = x #.append((v, x))
            adj_list[v][u] = 1/x #.append((u, 1/x))


        def dfs(s, t, val, visited):
            # if s==t:
                # return val
            # print(s)
            if t in adj_list[s]:
                if adj_list[s][t]==-1:
                    v = -1
                else:
                    v = val*adj_list[s][t]
                # print(s,'/',t, '=', v)
                return v
            
            visited.add(s)
            for nbr in adj_list[s].keys():
                if nbr not in visited:
                    ret = dfs(nbr, t, val * adj_list[s][nbr], visited)
                    if ret > 0:
                        return ret

            return -1


        ans = []
        for i in range(len(queries)):
            s, t = queries[i]
            visited = set()            
            if s in adj_list and t in adj_list:
                ret = dfs(s, t, 1.0, visited)
                # adj_list[s][t] = ret
            else:
                ret = -1
            ans.append(ret)

        return ans


            

        