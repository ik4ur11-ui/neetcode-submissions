class Solution:
    def isValid(self, s: str) -> bool:

        open_brackets = ["{", "(", "["]
        stack = []
        
        types = {"{": "curly", 
                "(": "round", 
                "[": "square", "}": "curly", 
                ")": "round", 
                "]": "square"}
        
        
        for i in s:
            if i in open_brackets:
                stack.append(types[i])
            else:
                if len(stack) != 0:
                    recent = stack.pop()
                    if types[i] != recent:
                        return False
                else:
                    return False
        
        if len(stack) == 0:
            return True
        
        return False