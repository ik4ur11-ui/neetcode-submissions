class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            universal = ''.join(sorted(s))
            #anagrams[universal] = anagrams.get(universal,[])
            anagrams[tuple(sorted(s))].append(s)
            
        categories = list(anagrams.values())

        return sorted(categories, key=len)