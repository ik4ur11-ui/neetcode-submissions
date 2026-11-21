
class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        sanitised_string = ""
        for i in s:
            if (i.isalnum()):
                sanitised_string += i

        print(sanitised_string)



        return sanitised_string[::-1] == sanitised_string
        
        