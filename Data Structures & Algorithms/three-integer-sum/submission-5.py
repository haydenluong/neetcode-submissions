class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        res = []
        # 1,2, x -> in order for this to be a triplet
        # x = - (1+2)
        # the target becomes -(1+2)
        nums.sort()
        # [-4, -1, -1, 0, 1, 2] 
        # l = -4, r = 2
        # target = -(-4+2) = 2 no 2
        # l = -4, 1 -> target = 3
        # l = -1, 1 -> target = 0
        # finds target -> append
        # l = -1
        # identify target first and then use 2 pointers? 
        # if so how do we get the target

        for i in range(0, len(nums)):
            # if i > 0 and nums[i] == nums[i-1]:
            #     continue
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            # if target is final then it couldnt be checked
            l, r = i+1, len(nums)-1
            while l < r: 
                if nums[l] + nums[r] > target:
                    r = r-1
                    continue
                elif nums[l] + nums[r] < target:
                    l = l+1
                    continue
                else: 
                    res.append([-target, nums[l], nums[r]])
                    l += 1
                    r -= 1 

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r-= 1  
        ## [-4, -1, -1, 0, 1, 2] 

        return res 