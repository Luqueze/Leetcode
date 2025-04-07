class Solution(object):
    def longestPalindrome(self, s):
        if len(s) <= 1:
            return 1
        
        count = 0

        while len(s) > 0:
            first_char = s[0]
            ocurrencies = s.count(first_char)

            if ocurrencies % 2 == 0:
                count += 2 * (ocurrencies // 2)

            s = s.replace(first_char,'')

        if len(s) > 0:
            count += 1

        if count > 2 and count % 2 == 0:  # Palíndromo é par e maior que 2
            count += 1  # Adiciona o caractere ímpar ao centro

        return count
    
        