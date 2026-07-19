class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target :
                return 0
            else :
                return -1
        l = 0
        r = len(nums)- 1
        while l < r:
            if nums[l] == target : return l
            if nums[r] == target : return r
            mil = int((r+l)/2)
            if nums[mil] == target : return mil
            if nums[mil] >= nums[l]:
                if nums[mil] > target and nums[l] < target :
                    r = mil -1
                else :
                    l = mil + 1
            else:
                if target > nums[mil] and target < nums[r]:
                    l = mil + 1
                else :
                    r = mil - 1
        return -1