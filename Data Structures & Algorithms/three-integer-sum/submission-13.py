class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        three_sum_combination = {}
        output = []
        

        for idx, n in enumerate(nums):
            complement = 0 - n
            seen = {}

            for i,c in enumerate(nums):
                if i != idx:
                    second_complement = complement - c
                    if second_complement in seen:
                        t = (n,c,second_complement)
                        three_sum_combination[tuple(sorted(t))] = ""
                    else:
                        seen[c] = ""

        for m,n in three_sum_combination.items():
            output.append(list(m))   

        return output
