from collections import Counter
class Solution:
    def uniqueId(self, arr):
        freq=Counter(arr)
        return freq.keys()
    
