class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window with a left pointer, subsequent right pointer
        #  
        l = 0
        charSet = set()
        res = 0
        for r in range(len(s)): 
            while s[r] in charSet:
                # if char is alr in set -> move left pointer 
                #  a b c a -> a b c -> a b c d (moves right pointer if not duplicated) - > a b c d a -> moes left pointer, to have b c d a ->
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res 