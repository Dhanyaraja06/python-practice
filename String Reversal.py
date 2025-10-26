class Solution:
    def reverseString(self, s):
        chars = []
        
        for ch in s[::-1]:     
            if ch != " " and ch not in chars:
                chars.append(ch)
        return "".join(chars)
