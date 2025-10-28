class Solution:
	def firstAlphabet(self, S):
        words = S.split()           
        result = ""
        for w in words:
            result += w[0]
        return result
