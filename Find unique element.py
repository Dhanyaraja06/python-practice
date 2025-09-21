from collections import Counter 
class Solution:
    def find_unique(self, k, arr):
        freq=Counter(arr)
        
        for num,Count in freq.items():
            if Count%k!=0:
               return num
