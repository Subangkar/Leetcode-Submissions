class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key=lambda x: (x[1], x[0]))
        # cur_s = points[0][0]
        cur_a = points[0][1]
        count_a = 1

        for i in range(1, len(points)):
            if cur_a < points[i][0]:
                count_a += 1
                cur_a = points[i][1]
            # cur_a = max(cur_a, points[0][1])
        return count_a


        