class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            universal = ''.join(sorted(s))
            #anagrams[universal] = anagrams.get(universal,[])
            anagrams[universal].append(s)

        return list(anagrams.values())