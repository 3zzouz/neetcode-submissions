from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def buildStringTuple(s:str)-> tuple[int,...]:
            res = [0]*26
            for el in s:
                ordering = ord(el)-ord('a')
                res[ordering] +=1
            return tuple(res)
        res=[]
        dic : dict[tuple[int,...],list[str]] = defaultdict(list)
        for el in strs:
            dic[buildStringTuple(el)].append(el)
        return list(dic.values())