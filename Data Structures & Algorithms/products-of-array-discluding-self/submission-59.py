class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * (len(nums))

        

        p_total = 1
        s_total = 1

        for idx, n in enumerate(nums):
            if idx != 0:
                p_total = p_total * nums[idx-1]

            output[idx] = output[idx] * p_total

            
        

        for idx in range(len(nums)- 1,-1, -1):
            if idx != len(nums)-1:
                s_total = s_total * nums[idx+1]

            output[idx] = output[idx] * s_total

        
        return output
        