class Solution(object):
    def longestPalindrome(self, s):
        if len(s) <= 1:
            return len(s)  
        
        contador = 0
        has_odd = False  

        while len(s) > 0:
            first_char = s[0]  
            ocurrencies = s.count(first_char)

            # if there are more than one appearence of a number it will count it
            contador += 2 * (ocurrencies // 2)

            # verifies if a char appear odd time
            if ocurrencies % 2 == 1:
                has_odd = True

            # delete the chars of the string
            s = s.replace(first_char, '')

        # count + 1 if the size of the string is even
        if has_odd:
            contador += 1

        return contador