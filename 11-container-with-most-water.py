class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1

        maxarea = 0
        while left<right:
            width = right - left
            maxarea = max(width * min(height[left], height[right]), maxarea)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return maxarea
        