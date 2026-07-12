class Solution:
    def isPalindrome(self, s: str) -> bool:
        d = len(s) - 1
        g = 0
        while d > g:
            while not ('A'<=s[d].upper()<='Z' or '0'<=s[d]<='9') and d>g:
                d-=1
            while not ('A'<=s[g].upper()<='Z' or '0'<=s[g]<='9') and d>g:
                g+=1    
            if s[d].lower() != s[g].lower() : return False
            d-=1
            g+=1
        return True