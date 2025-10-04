from collections import Counter
class Solution:
    def findDuplicates(self, arr):
        freq=Counter(arr)
        new=[]
        for key,count in freq.items():
            if count==2:
                new.append(key)
        return new
            
