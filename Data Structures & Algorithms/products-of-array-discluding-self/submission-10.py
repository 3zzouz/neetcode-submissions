class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [int]*n
        post = [int]*n
        pref[0]=nums[0]
        post[n-1]=nums[n-1]
        for g in range(1,n):
            pref[g] = pref[g-1] * nums[g]
            d = n - 1 - g
            post[d] = post[d+1] * nums[d]
        res = [int]*n
        for i in range(n):
            p = 1
            if i+1 < n : p*=post[i+1]
            if i-1 >= 0 : p*=pref[i-1]
            res[i] = p
        return res
        
