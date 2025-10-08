
class Solution:
    def longest(self, arr):
        longest=""
        for i in arr:
            if len(i)>len(longest):
                longest=i
        return longest
