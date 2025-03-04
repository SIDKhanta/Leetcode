class Solution(object):
    def longestPalindrome(self, s):
        for i in range(len(s)):
            for j in range(i, len(s)):


s = input()
print(Solution.longestPalindrome(s))