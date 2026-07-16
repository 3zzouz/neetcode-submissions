from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        auxt = defaultdict(int)
        n = len(s)
        m = n+1
        r = 0
        l = 0
        res = ""
        for c in t:
            auxt[c]+=1
        x = len(auxt)
        while r < n and (s[r] not in auxt):
            r+=1                
        l = r
        aux_window = defaultdict(int)
        compt = 0
        while l<=r:
            while r<n and compt < x:
                aux_window[s[r]]+=1
                if s[r] in auxt and aux_window[s[r]] == auxt[s[r]]:
                    compt +=1
                r+=1
            if compt != x: break
            length_window = r - l
            if length_window < m :
                m = length_window
                res = s[l:r]
            aux_window[s[l]]-=1
            if s[l] in auxt and aux_window[s[l]] < auxt[s[l]]:
                compt -=1
            l+=1
            while l<n and s[l] not in auxt:
                aux_window[s[l]]-=1
                l+=1
        return res