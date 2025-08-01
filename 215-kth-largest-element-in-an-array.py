class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def quickselect(arr, k):
            """
            Returns the k-th smallest element in arr (0-indexed)
            """
            if len(arr) == 1:
                return arr[0]

            pivot = random.choice(arr)

            lows = [x for x in arr if x < pivot]
            highs = [x for x in arr if x > pivot]
            pivots = [x for x in arr if x == pivot]

            if k < len(lows):
                return quickselect(lows, k)
            elif k < len(lows) + len(pivots):
                return pivot
            else:
                return quickselect(highs, k - len(lows) - len(pivots))
        
        return quickselect(nums, len(nums)-k)
        