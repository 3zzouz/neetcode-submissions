from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s : dict[int,int]= defaultdict(int)
        res = set()
        for id,el in enumerate(nums):
            s[el]=id
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                rest = -(nums[i]+nums[j])
                if rest in s and s[rest] != i and s[rest]!=j:
                    res.add(tuple(sorted([nums[i],nums[j],rest])))
        return [list(i) for i in res]