class Solution:
	def pushZerosToEnd(self, arr):
	    n=len(arr)
	    number=[]
	    zeros=[]
    	for i in range(n):
    	    if arr[i]!=0:
    	       number.append(arr[i])
    	    else:
    	       zeros.append(arr[i])
        index=0
        for i in number:
            arr[index]=i
            index+=1
        for i in zeros:
            arr[index]=i
            index+=1
       
