class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += str(len(word))
            encoded_string += "@"
            encoded_string += word
        
        print(encoded_string)
        return encoded_string


    def decode(self, s: str) -> List[str]:
        output = []
        while s != "":
            end = 0
            for i in s:
                if i == "@":
                    break
                end += 1
            
            n = int(s[0:end])
            

            output.append(s[end+1:n+end+1])
            
            s = s[n+end+1:]
            

        return output
