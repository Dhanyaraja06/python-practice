class Solution:
    def uncommonChars(self, s1, s2):
        unique_s1=""
        unique_s2=""
        for i in s1:
            if i not in s2 and i not in unique_s1:
                unique_s1+=i
            else:
                continue
        for j in s2:
            if j not in s1 and not j in unique_s2:
                unique_s2+=j
        result=''.join(sorted(unique_s1 + unique_s2))
        
        return result
