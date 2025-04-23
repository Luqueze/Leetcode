import sys
sys.set_int_max_str_digits(0)  

class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        
        resultado = str(int("".join(map(str, num))) + k)
        return list(map(int, resultado))

