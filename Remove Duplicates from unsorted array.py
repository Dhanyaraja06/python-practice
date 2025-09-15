class Solution:
    def removeDuplicate(self, arr):
        seen = set()
        result = []
        
        for element in arr:
            if element not in seen:
                seen.add(element)
                result.append(element)
        
        return result
