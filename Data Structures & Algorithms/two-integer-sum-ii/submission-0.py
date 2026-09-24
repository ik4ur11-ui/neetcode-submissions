class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        seen = {}
        for idx,n in enumerate(numbers):
            complement = target - n
            if complement in seen:
                return [seen[complement], idx+1]
            else:
                seen[n] = idx+1


        