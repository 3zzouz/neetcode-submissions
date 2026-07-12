class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s= {}
        for ind,el in enumerate(nums):
            rest = target - el
            if rest in s and s[rest]!=ind : return [s[rest],ind]
            s[el] = ind 
        