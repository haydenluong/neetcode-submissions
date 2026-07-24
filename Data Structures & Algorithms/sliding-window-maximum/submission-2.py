class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        res = []
        maxNum = float("-inf")

        # 2,0 ; 3,1 ; 4, 2
        # r - (k - 1) = 2 - 2, 3 - 2. 4 - 2

        for r in range(k-1, len(nums)):
            maxNum = float("-inf")
            for i in range(r-(k-1), r+1): 
                maxNum = max(nums[i], maxNum)
            res.append(maxNum)
        return res 

