from collections import Counter

class Solution:
    def getCount(self, S, N):
        final = []
        first_letter = ''
        for char in S:
            if char != first_letter:
                final.append(char)
                first_letter = char

        freq = Counter(final)

        count = 0
        for value in freq.values():
            if value == N:
                count += 1
        
        return count
