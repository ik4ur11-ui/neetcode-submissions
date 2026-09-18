class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        positions = []
        for idx, n in enumerate(nums):
            complement = target - n
            if complement in seen:
                positions.append(seen[complement])
                positions.append(idx)
            seen[n] = idx
        
        return positions
