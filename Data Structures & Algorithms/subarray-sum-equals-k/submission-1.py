from collections import Counter
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        prefixSum = 0

        seen = Counter()

        seen[0] = 1

        for num in nums:
            prefixSum += num

            needed = prefixSum - k
            
            count += seen[needed]

            seen[prefixSum] += 1

        return count


        