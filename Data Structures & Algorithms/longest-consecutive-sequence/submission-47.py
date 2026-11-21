class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        

        nums = list(set(nums))
        

        nums.sort()

        idx = 0
        longest = 1
        current = 1
        
        print(nums)

        while idx < len(nums) - 1:
            if nums[idx+1] - 1 == nums[idx]:
                current += 1
            else:
                current = 1
                
            longest = max(current,longest)
            
            idx += 1
        
        return longest

        

