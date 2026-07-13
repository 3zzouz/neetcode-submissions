class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        aux = set()
        l = 0
        r = 0
        m = 0
        while r<len(s):
            print(aux)
            if s[r] in aux :
                m = max(m,len(aux))
                print(m)
                while s[r] in aux :
                    aux.remove(s[l])
                    l+=1
            else :
                aux.add(s[r])
                r+=1
        return max(m,len(aux))