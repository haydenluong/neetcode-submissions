class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # lecabee

        if len(s1) > len(s2):
            return False

        cnt_s1 = Counter(s1)
        track = {}

        l = 0 
        for r in range(len(s1)):
            track[s2[r]] = track.get(s2[r], 0) + 1 
            if track == cnt_s1:
                return True

        for r in range(len(s1), len(s2)):
            track[s2[l]] -= 1
            if track[s2[l]] == 0:
                del track[s2[l]]
            l += 1

            track[s2[r]] = track.get(s2[r], 0) + 1

            if track == cnt_s1:
                return True

        return False

        




