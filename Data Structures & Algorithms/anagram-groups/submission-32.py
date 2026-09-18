class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for s in strs:
            universal = ''.join(sorted(s))
            anagrams[universal] = anagrams.get(universal,[])
            anagrams[universal].append(s)
            
        categories = list(anagrams.values())

        return sorted(categories, key=len)