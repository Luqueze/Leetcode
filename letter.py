from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = {
            2: ['a', 'b', 'c'],
            4: ['d', 'e', 'f'],
            5: ['g', 'h', 'i'],
            6: ['j', 'k', 'l'],
            7: ['m', 'n', 'o'],
            8: ['p', 'q', 'r', 's'],
            9: ['w', 'x', 'y', 'z']
        }

def letter_combinations(digits):
    # Verifica se a entrada está vazia
    if not digits:
        return []

    # Função auxiliar para realizar o backtracking
    def backtrack(index, path):
        # Caso base: se o caminho atual tiver o mesmo comprimento que os dígitos
        if index == len(digits):
            combinations_list.append("".join(path))
            return

        # Obter as letras correspondentes ao dígito atual
        possible_letters = combinations[int(digits[index])]
        for letter in possible_letters:
            # Adiciona a letra ao caminho atual e continua a busca
            backtrack(index + 1, path + [letter])

    # Lista para armazenar todas as combinações
    combinations_list = []
    backtrack(0, [])
    return combinations_list

# Exemplo de uso
digits = "234"  # Digite os números aqui
result = letter_combinations(digits)
print(result)

