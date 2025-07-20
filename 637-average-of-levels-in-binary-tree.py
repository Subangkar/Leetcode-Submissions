from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level_sums = []
        level_counts = []
        # level = 0
        q = deque()
        q.append((root, 1))
        while q:
            node, level = q.popleft()
            if len(level_sums)<level:
                level_sums.append(node.val)
                level_counts.append(1)
            else:
                level_sums[level-1] += node.val
                level_counts[level-1] += 1
            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))
        return [x/y for x,y in zip(level_sums, level_counts)]