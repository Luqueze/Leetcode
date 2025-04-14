class Solution(object):
    def maxProfit(self, prices):
        
        maior = 0
        menor = float('inf')
        lucro = 0  

        for i in prices:
            if i < menor:
                menor = i
            elif i - menor > lucro:  
                lucro = i - menor

        return lucro 