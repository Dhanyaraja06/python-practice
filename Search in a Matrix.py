import numpy as np
class Solution:
    def searchMatrix(self,matrix, x): 
        flattened = np.array(matrix).flatten()
        for i in flattened:
            if i==x:
                return True
        return False
                
    	
