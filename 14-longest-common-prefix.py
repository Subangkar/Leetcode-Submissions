class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i]!=strs[-1][i]:
                return strs[0][:i]
        return strs[0][:min(len(strs[0]), len(strs[-1]))]