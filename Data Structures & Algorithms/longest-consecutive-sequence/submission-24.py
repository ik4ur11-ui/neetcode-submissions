class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        
        
        lst = list(set(nums))
        lst.sort()
        print(lst)
        current_max = 1
        consecutives = []
        for i in range (len(lst)-1):
            if lst[i+1] - 1 == lst[i]:
                current_max +=1
            else:
                consecutives.append(current_max)
                current_max = 1
        consecutives.append(current_max)
        print(consecutives)
        output = max(consecutives)
        return output