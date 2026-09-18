class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            universal = ''.join(sorted(s))
            if universal in anagrams:
                anagrams[universal].append(s)
            else:
                anagrams[universal] = [s]

        categories = []

        for i in anagrams:
            categories.append(anagrams[i])


        output = sorted(categories, key=len)
        return output