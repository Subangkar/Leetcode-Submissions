class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged_list = []
        cur_s = intervals[0][0]
        cur_e = intervals[0][1]
        for i in range(1, len(intervals)):
            if cur_e >= intervals[i][0]:
                cur_e = max(cur_e, intervals[i][1])
            else:
                merged_list.append([cur_s, cur_e])
                cur_s = intervals[i][0]
                cur_e = intervals[i][1]

        merged_list.append([cur_s, cur_e])        
        return merged_list
        