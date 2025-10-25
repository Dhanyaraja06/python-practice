class Solution:
    def armstrongNumber (self, n):
        num= n
        sum=0
        for i in str(num):
            digit=int(i)
            sum+=digit**3
        return sum==num
