class Solution(object):
    def longestPalindrome(self, s):
        if len(s) <= 1:
            return s
        
        biggest = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                substring = s[i:j]
                if substring == substring[::-1] and len(substring) > biggest:
                    biggest = len(substring)
        return biggest           
        