class Solution(object):
    def plusOne(self, digits):
        maior = -1
        indexx = -1

        for i in range(len(digits)):      
            if digits[i] > maior:
                maior = digits[i]
                indexx = i

        digits[indexx] = digits[indexx] + 1    

        return digits