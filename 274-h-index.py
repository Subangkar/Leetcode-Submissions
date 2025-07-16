class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        h = 0
        for i in range(n-1, -1, -1):
            if citations[i]<=(n-i):
                h = max(h, citations[i])
                break
            if citations[i]>(n-i):
                h = max(h, n-i)
        # if h==0 and citations[n-1]>0:
        #     return 1
        return h
        