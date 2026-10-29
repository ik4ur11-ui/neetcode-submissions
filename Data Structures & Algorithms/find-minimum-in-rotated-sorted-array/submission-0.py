import math

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        middle = len(nums) // 2

        lowest = math.inf

        nums = sorted(nums)

        while nums:
            if nums[middle] < lowest:
                lowest = nums[middle]
                nums = nums[:middle]
            else:
                nums = nums[middle:]
            middle = len(nums) // 2
        
        return lowest
            