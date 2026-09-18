class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueList = set(nums)
        
        return (len(uniqueList) != len(nums))
        