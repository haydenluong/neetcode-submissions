class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxV = 0 
        l, r = 0, len(heights)-1
        while l < r: 
            area = min(heights[l], heights[r]) * (r-l)
            maxV = max(maxV, area)
            if heights[l] >= heights[r]:
                r -= 1
            elif heights[r] > heights[l]:
                l+=1
        return maxV

# when heights[l] < heights[r] the area is (r-l) * heights[l]
# if we keep l fixed and move r, the area can only be equal or worse than the first one
# therefore, we move l in hope of finding a taller wall, which compensates for the shorter distance 