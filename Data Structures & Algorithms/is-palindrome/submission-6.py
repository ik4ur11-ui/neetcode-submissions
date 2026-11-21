
class Solution:
    def isPalindrome(self, s: str) -> bool:

        
        sanitised_string = ""
        for i in s:
            if (i.isalnum()):
                sanitised_string += i.lower()

        print(sanitised_string)



        return sanitised_string[::-1] == sanitised_string
        
        