class Solution:

    def kthSmallest(self, arr,k):
        sorted_array=sorted(arr)
        for i in range(len(arr)):
            return sorted_array[k-1]
