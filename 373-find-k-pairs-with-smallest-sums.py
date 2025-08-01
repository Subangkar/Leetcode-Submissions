class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m = len(nums1)
        n = len(nums2)

        vis = set()
        pairs = []
        pq = []

        heapq.heappush(pq, (nums1[0]+nums2[0], (0,0)))
        vis.add((0, 0))

        while pq and len(pairs) < k:
            _, (i, j) = heapq.heappop(pq)
            pairs.append((nums1[i], nums2[j]))
            if i+1<m and (i+1, j) not in vis:
                heapq.heappush(pq, (nums1[i+1]+nums2[j], (i+1, j)))
                vis.add((i+1, j))
            if j+1<n and (i, j+1) not in vis:
                heapq.heappush(pq, (nums1[i]+nums2[j+1], (i, j+1)))
                vis.add((i, j+1))
            # print(pq)
        
        return pairs

        