from typing import List
from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Mapeamento de dígitos para letras (como em teclados de telefone)
        combinations = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        # Verifica se a entrada está vazia
        if not digits:
            return []

        # Gera as combinações cartesianas usando itertools.product
        letters = [combinations[digit] for digit in digits]
        return [''.join(comb) for comb in product(*letters)]

# Exemplo de uso
solution = Solution()
digits = "234"  # Digite os números aqui
result = solution.letterCombinations(digits)
result  # Apenas retorna o resultado