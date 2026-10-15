class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d={}
        for x in nums:
            d[x]=d.get(x,0)+1
        if len(d)<len(nums):
            return True
        return False
        
