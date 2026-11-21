from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = defaultdict(int)
        
        for idx, n in enumerate(nums):
            complement = target - n

            if complement in seen:
                output = [seen[complement],idx]

            seen[n] = idx
        
        return output

