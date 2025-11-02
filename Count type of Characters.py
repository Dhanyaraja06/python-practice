class Solution:
    def count(self, s):
        lower = 0
        upper = 0
        digit = 0
        special = 0

        for ch in s:
            if ch.islower():
                lower += 1
            elif ch.isupper():
                upper += 1
            elif ch.isdigit():
                digit += 1
            else:
                special += 1

        return [upper, lower, digit, special]
