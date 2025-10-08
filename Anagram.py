from collections import Counter
class Solution:
    def areAnagrams(self, s1, s2):
        str1=Counter(s1)
        str2=Counter(s2)
        return str1==str2
        
                  
