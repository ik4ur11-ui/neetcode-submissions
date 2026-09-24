class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alpha_list = []
        for c in s:
            if c.isalnum():
                alpha_list.append(c)

        print(alpha_list)
        print(list(reversed(alpha_list)))
        return list(reversed(alpha_list)) == alpha_list