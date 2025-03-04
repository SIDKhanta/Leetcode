class Solution(object):
    dict = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000,
        'IV' : 4,
        'IX' : 9,
        'XL' : 25,
        'XC' : 90,
        'CD' : 400,
        'CM' : 900
    }
    def romanToInt(self, s, result = 0):
        i = 0
        while i < len(s):
            if i + 2 <= len(s) and s[i:i + 2] in Solution.dict.keys():
                result += Solution.dict[s[i:i + 2]]
                i += 2
            else:
                result += Solution.dict[s[i:i + 1]]
                i += 1
        return result