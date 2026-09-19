class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        string = ""
        for s in strs:
            string += str(len(s))
            string += "#"
            string += s
        print("s" , string)
        return string

    def decode(self, s: str) -> List[str]:
        lst = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j+= 1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            lst.append(word)
            i = j + length + 1
            
        return lst