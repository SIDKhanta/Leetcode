class Solution(object):
    def lengthOfLongestSubstring(self, s, mx = 1):
        if s == '':
            return 0
        if len(s) == 1:
            return 1
        index = 0
        elems = {s[0] : 0}
        for i in range(1, len(s)):
            if s[i] in elems:
                for el in s[index:elems[s[i]]]:
                    del elems[el]
                mx = max(mx, i - index)
                index = elems[s[i]] + 1
                elems[s[i]] = i
            else:
                elems[s[i]] = i
        return max(mx, i - index + 1)