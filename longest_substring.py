class Solution(object):
    def lengthOfLongestSubstring(self, s):
        copy = ''
        size = 1
        for i in range(len(s)):
            if s[i] in copy:
               copy = copy[copy.index(s[i]) + 1:]
            copy += s[i]   

            size = max(size, len(copy))
            
        return size    


