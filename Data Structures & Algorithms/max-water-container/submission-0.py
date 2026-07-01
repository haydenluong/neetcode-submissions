class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxV = 0 
        iti = 0
        l, r = 0, len(heights)-1
        while l < r: 
            if heights[l] >= heights[r]:
                var = (r-l) * heights[r]
                if var > maxV:
                    maxV = var
                    # iti = r
                r -= 1
            elif heights[r] > heights[l]:
                var = (r-l) * heights[l]
                if var > maxV:
                    maxV = var
                    # iti = r
                l+=1
        return maxV
        # return iti