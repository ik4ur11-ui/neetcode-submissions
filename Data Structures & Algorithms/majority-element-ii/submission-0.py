from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        frequencies = Counter(nums)
        output = []

        frequencies = dict(sorted(frequencies.items(), key=lambda x:-x[1]))

        k = len(nums) // 3

        print(k)

        for (n,c) in frequencies.items():
            if c <= k:
                break
            output.append(n)
        
        print(frequencies)


        return output
        
