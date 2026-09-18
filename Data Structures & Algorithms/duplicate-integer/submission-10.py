class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueList = set(nums)
        print(len(nums))
        print(len(uniqueList))
        
        
        return (len(uniqueList) != len(nums))
        