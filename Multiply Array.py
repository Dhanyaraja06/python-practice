class Solution:
    def longest(self, arr, n):
        product=1
        for i in range(n):
            product *= arr[i]
        return product
