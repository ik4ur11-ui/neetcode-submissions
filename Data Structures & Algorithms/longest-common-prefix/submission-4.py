class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        current = ""
        idx = 0

        if len(strs) == 1:
            return strs[0]

        end = min(len(strs[0]), len(strs[1]))
        
        while idx < len(strs) - 1:
            word = strs[idx]
            next = strs[idx + 1]
            print(word)
            print(next)
            if word[:end] == next[:end]:
                current = word[:end]
                print(current)
                idx += 1
            else:
                end -= 1
        return current

