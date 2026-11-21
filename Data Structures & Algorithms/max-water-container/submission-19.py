class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1
        largest = 0

        while l < r:
            width = r - l
            height = min(heights[l],heights[r])
            area = width * height
            largest = max(largest, area)

            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1

        return largest
        