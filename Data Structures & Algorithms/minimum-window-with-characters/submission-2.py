class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # struggles with
            # computing the value of have
            # Counter() not Counter(s)

        res = [-1, -1]
        resLen = float("inf")

        cnt = Counter(t) #X: 1, Y:1, Z: 1
        cnt_s = Counter()

        have = 0 
        need = len(cnt)

        l = 0
        for r in range (len(s)): # s -> 10
            cnt_s[s[r]] += 1

            if s[r] in cnt and cnt_s[s[r]] == cnt[s[r]]:
                have += 1

            while have == need: 
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res =[l, r]
                
                cnt_s[s[l]] -= 1
                if s[l] in cnt and cnt_s[s[l]] < cnt[s[l]]:
                    have -=1 
                l += 1 
        
        l, r = res 
        return s[l:r+1] if resLen != float("infinity") else ""
                    


            # if s[r] is not in t, then 






        # 
        
        # find the first word of t in s -> window starts from there (but what abt shrinking the window?)

        #  

        # return in string slicing 