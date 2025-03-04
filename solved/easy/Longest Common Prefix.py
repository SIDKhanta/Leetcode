class Solution(object):
    def longestCommonPrefix(self, strs, result = ''):
        strs.sort(key = len)
        for index in range(len(strs[0])):
            for i in range(1, len(strs)):
                if strs[0][index] != strs[i][index]:
                    return result
            result += strs[0][index]
        return result