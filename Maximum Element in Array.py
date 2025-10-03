class Solution:
    def largest(self, arr : List[int]) -> int:
        new=sorted(arr)
        return new[-1]
