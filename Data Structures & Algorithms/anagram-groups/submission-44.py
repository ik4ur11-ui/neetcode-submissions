from collections import defaultdict
class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list) #instead of [str] we need list here

        for word in strs:
            key = tuple(sorted(word))
            anagrams[key].append(word) # sorted(word) is of type list
            # LISTS cannot be keys for dictiionaries since they are mutable

        
        return (list(anagrams.values()))
        