class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1={}
        map2={}
        for c in s:
            if c not in map1 : map1[c]=0
            map1[c] = map1[c] +1 
        for c in t:
            if c not in map2 : map2[c]=0
            map2[c] = map2[c]+1
        for el in map1.keys():
            if el not in map2 : return False
            if map1[el] != map2[el] : return False
        for el in map2.keys():
            if el not in map1 : return False
            if map1[el] != map2[el] : return False
        return True
