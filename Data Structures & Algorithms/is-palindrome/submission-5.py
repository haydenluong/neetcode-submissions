class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers -> compare l and r -> if not matched, return false
        # r[-1] -> r[-1-1] -> r[-1-1-1]
        new_str = "".join(ch for ch in s if ch.isalnum())
        l, r = 0, len(new_str) - 1
        while l < r: 
            if new_str[l].lower() != new_str[r].lower():
                return False
            l += 1
            r -= 1
        return True

            # how do i remove/ignore the spaces in the string 