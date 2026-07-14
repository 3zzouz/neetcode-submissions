class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        aux = [-1] * 26
        n = len(s2)
        x = len(s1)
        for c in s1:
            if aux[ord(c)-ord('a')] == -1 : aux[ord(c)-ord('a')] = 0
            aux[ord(c)-ord("a")]+=1
        l = 0
        r = 0
        while r<n :
            while r < n and aux[ord(s2[r])-ord('a')] == -1:
                r+=1
                while l<r :
                    if aux[ord(s2[l])-ord('a')] > -1:
                        aux[ord(s2[l])-ord('a')]+=1
                    l+=1
            if r < n and aux[ord(s2[r])-ord('a')] >= 1:
                aux[ord(s2[r])-ord('a')]-=1
                r+=1
            elif r < n and aux[ord(s2[r])-ord('a')] < 1:
                aux[ord(s2[l])-ord('a')] += 1
                l+=1
            if r-l == x: return True
        return False
