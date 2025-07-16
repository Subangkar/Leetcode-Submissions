class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        max_diff = -1 # can be at least 0 since there is a solution and it cannot be negative
        cur_diff = 0
        s = -1
        for i in range(len(gas)-1, -1, -1):
            cur_diff += gas[i]-cost[i]
            if cur_diff>max_diff:
                # start from the point where the difference is the highest check from the opposite direction since we move from i->i+1
                max_diff = cur_diff
                s = i
        return s
        