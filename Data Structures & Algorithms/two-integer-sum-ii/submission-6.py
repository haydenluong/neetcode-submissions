class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # create a dictionary : number-index pair 
        # or use enumerate 
        # how do i compare ? using two pointers 
        # 1 and 4 = 5 -> 1 and 3 = 4 1 -> 

        l, r = 0, len(numbers)-1
        while l < r: 
            if numbers[l] + numbers[r] > target:
                r = r-1
                continue
            elif numbers[l] + numbers[r] < target:
                l = l+1
                continue
            else:
                return [l+1, r+1]
        return []

        # append into res 