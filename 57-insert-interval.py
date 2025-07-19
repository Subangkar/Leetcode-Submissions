class Solution:
    def insert(self, intervals, newInterval):
        
        index = -1 # keep interval ends before me # this will not work if intervals are overlapping
        l = 0
        r = len(intervals)-1
        while l<=r:
            m = (l+r)//2
            if intervals[m][1] < newInterval[0]:
                l = m+1
                index = m
            elif intervals[m][1] >= newInterval[0]:
                r = m-1
        
        # print(index)
        # left nonoverlapping
        merged = intervals[:index+1] + [newInterval]
        # print(merged)
        index = index+1
        # merge right overlapping
        for i in range(index, len(intervals)):
            if merged[-1][1] < intervals[i][0]:
                index = i
                break
            else:
                merged[-1][0]=min(merged[-1][0], intervals[i][0])
                merged[-1][1]=max(merged[-1][1], intervals[i][1])
                index = i+1
        # print(merged)

        # merge right nonoverlapping
        if index < len(intervals):
          merged = merged + intervals[index:]
        # print(merged)

        return merged
