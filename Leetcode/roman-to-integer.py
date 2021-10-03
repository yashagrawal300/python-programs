# 
# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        exceptions = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        for ex in exceptions.keys():
            if ex in s:
                total += exceptions[ex]
                s = s.replace(ex, '')
        for i in range(len(s)):
            total += romans[s[i]]
        return total
