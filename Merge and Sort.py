from collections import Counter
class Solution:
    def mergeNsort(self, arr1, arr2):
        merged=arr1+arr2
        freq=Counter(merged)
        keys=list(freq.keys())
        return sorted(keys)
