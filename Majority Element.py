from collections import Counter
class Solution:
    def majorityElement(self, arr):
        length=len(arr)//2
        freq=Counter(arr)
        for key, count in freq.items():
            if count>length:
                return key
            
        return -1
                
            
