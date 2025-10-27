from collections import Counter
class Solution:
    def firstRep(self, s):
        count = Counter(s)
        for i in s:
            if count[i] > 1:
                return ch
        return '#'
