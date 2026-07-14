class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        aux = {}
        n = len(s2)
        x = len(s1)
        for c in s1:
            if c not in aux : aux[c] = 0
            aux[c]+=1
        cop = aux.copy()
        l = 0
        r = 0
        while r<n :
            isskipping = False
            while r < n and s2[r] not in aux:
                r+=1
                isskipping = True
            if isskipping :
                aux = cop.copy()
                l = r
            if r < n and s2[r] in aux and aux[s2[r]] >= 1:
                aux[s2[r]]-=1
                print('+++',s2[r])
                r+=1
            elif r < n and s2[r] in aux and aux[s2[r]] < 1:
                aux[s2[l]] += 1
                print('---',s2[l])
                l+=1
            print(l,r,aux)
            if r-l == x: return True
        return False
