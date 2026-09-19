class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        freq = [[] for i in range (len(nums) + 1)]
        for n in nums:
            counts[n] += 1

        for n, c in counts.items():
            freq[c].append(n)
        
        
        kElements = []
        for i in range (len(nums),0, -1):
            for n in freq[i]:
                if len(kElements) == k:
                    break
                kElements.append(n)
        return kElements
        
        